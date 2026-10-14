#!/usr/bin/env python3
"""Build a mixed, ranked 1,500-problem interview-practice list.

The input repositories are external snapshots. This script stores no problem
statements or solutions; it combines titles, URLs, difficulty, topics, company
tags, recency windows, and curated-list membership.
"""

from __future__ import annotations

import argparse
import csv
import math
import re
from collections import defaultdict, deque
from pathlib import Path
from typing import Any


TIER_SIZES = [
    ("Must solve", 250),
    ("Strong priority", 350),
    ("Breadth builder", 450),
    ("Useful if time", 300),
    ("Meh / optional", 150),
]

FAMILY_TARGETS = {
    "Arrays, hashing, counting": 120,
    "Strings, parsing, tries": 90,
    "Two pointers, sliding window": 90,
    "Prefix sums, intervals, sweep line": 85,
    "Binary search, selection": 75,
    "Sorting, greedy": 95,
    "Stack, queue, monotonic structures": 75,
    "Linked lists": 35,
    "Trees, BST": 110,
    "Graph traversal, topo, union-find": 115,
    "Shortest paths, MST, advanced graphs": 60,
    "Heaps, streams, ordered sets": 60,
    "Backtracking, combinatorial search": 65,
    "1D DP, knapsack": 90,
    "Advanced DP": 105,
    "Math, combinatorics": 55,
    "Bit manipulation": 35,
    "Data-structure design, caches": 65,
    "Matrix, grid, geometry": 45,
    "Randomized, concurrency, specialized": 30,
}

COMPANY_WEIGHTS = {
    # Primary targets
    "Waymo": 18,
    "Google": 14,
    "Meta": 10,
    "LinkedIn": 10,
    # AI, data, and infrastructure
    "OpenAI": 8,
    "Anthropic": 8,
    "Nvidia": 6,
    "Databricks": 6,
    "Snowflake": 6,
    "Palantir": 5,
    "Cloudflare": 5,
    "Confluent": 5,
    "MongoDB": 5,
    "Dropbox": 4,
    # FAANG+ and high-volume top tech
    "Amazon": 5,
    "Microsoft": 5,
    "Apple": 5,
    "Netflix": 4,
    "Uber": 5,
    "Airbnb": 5,
    "Stripe": 5,
    "DoorDash": 5,
    "Snap": 5,
    "TikTok": 5,
    "ByteDance": 4,
    "Spotify": 4,
    "Roblox": 4,
    "Atlassian": 4,
    "Salesforce": 4,
    "Adobe": 4,
    "Oracle": 3,
    "Intel": 3,
    "AMD": 3,
    # Autonomous vehicles and mobility
    "Tesla": 5,
    "Cruise": 5,
    "Rivian": 4,
    "Applied Intuition": 5,
    "Aurora": 5,
    "Lyft": 4,
    "Instacart": 4,
    # Finance and trading
    "Citadel": 5,
    "Jane Street": 5,
    "Two Sigma": 5,
    "DE Shaw": 5,
    "Bloomberg": 5,
    "Goldman Sachs": 3,
    "Robinhood": 4,
    "Coinbase": 4,
    "Block": 4,
}

PRIORITY_COMPANIES = ["Waymo", "Google", "Meta", "LinkedIn"]

CURATED_WEIGHTS = {
    "top-interview-150": 12,
    "neetcode-150": 10,
    "grind-75": 10,
    "grind-169": 8,
    "neetcode-250": 8,
    "google-top": 10,
    "meta-top": 7,
    "blind-75": 8,
    "sean-prashad-patterns": 5,
    "striver-sde": 4,
    "striver-a2z": 3,
    "algomap-100": 5,
    "amazon-top": 3,
}

RECENCY_FILES = {
    "1. Thirty Days.csv": ("30d", 10),
    "2. Three Months.csv": ("3m", 7),
    "3. Six Months.csv": ("6m", 4),
}

CURRENT_RECENCY_FILES = {
    "thirty-days.csv": ("30d", 10),
    "three-months.csv": ("3m", 7),
    "six-months.csv": ("6m", 4),
}

ROTATION_GROUPS = [
    ["Arrays, hashing, counting", "Strings, parsing, tries", "Two pointers, sliding window"],
    ["Trees, BST", "Graph traversal, topo, union-find", "Shortest paths, MST, advanced graphs"],
    ["1D DP, knapsack", "Advanced DP", "Backtracking, combinatorial search"],
    ["Sorting, greedy", "Binary search, selection", "Heaps, streams, ordered sets"],
    ["Prefix sums, intervals, sweep line", "Stack, queue, monotonic structures", "Data-structure design, caches"],
    ["Linked lists", "Math, combinatorics", "Bit manipulation", "Matrix, grid, geometry", "Randomized, concurrency, specialized"],
]

NON_ALGORITHM_SLUGS = {
    line.strip()
    for line in Path(__file__).with_name("non_algorithm_slugs.txt").read_text(encoding="utf-8").splitlines()
    if line.strip() and not line.startswith("#")
}


def normalize_url(value: str) -> str:
    value = value.strip().split("?")[0].rstrip("/")
    return value.replace("http://", "https://")


def normalize_name(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.lower())


def parse_number(value: str | None) -> float | None:
    if not value:
        return None
    match = re.search(r"-?\d+(?:\.\d+)?", value.replace(",", ""))
    return float(match.group()) if match else None


def empty_problem(url: str) -> dict[str, Any]:
    return {
        "url": url,
        "id": "",
        "title": "",
        "difficulty": "",
        "acceptance": None,
        "topics": set(),
        "companies": {},
        "curated": set(),
        "curated_patterns": [],
        "local_rank": None,
        "local_pattern": "",
        "contest_rating": None,
    }


def company_directories(root: Path) -> dict[str, Path]:
    return {normalize_name(path.name): path for path in root.iterdir() if path.is_dir()}


def find_company(root_index: dict[str, Path], company: str) -> Path | None:
    return root_index.get(normalize_name(company))


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def load_global_metadata(root: Path) -> dict[str, dict[str, Any]]:
    metadata: dict[str, dict[str, Any]] = {}
    for path in root.glob("*/all.csv"):
        for row in read_csv(path):
            url = normalize_url(row.get("URL", ""))
            if not url:
                continue
            item = metadata.setdefault(url, {})
            item.setdefault("id", row.get("ID", "").strip())
            item.setdefault("title", row.get("Title", "").strip())
            item.setdefault("difficulty", row.get("Difficulty", "").title())
            acceptance = parse_number(row.get("Acceptance %"))
            if acceptance is not None:
                item["acceptance"] = acceptance
    return metadata


def load_company_data(
    archive_root: Path,
    current_root: Path,
    metadata: dict[str, dict[str, Any]],
) -> dict[str, dict[str, Any]]:
    problems: dict[str, dict[str, Any]] = {}
    archive_index = company_directories(archive_root)
    current_index = company_directories(current_root)

    for company in COMPANY_WEIGHTS:
        archive_dir = find_company(archive_index, company)
        current_dir = find_company(current_index, company)

        if archive_dir:
            for row in read_csv(archive_dir / "5. All.csv"):
                url = normalize_url(row.get("Link", ""))
                if not url:
                    continue
                item = problems.setdefault(url, empty_problem(url))
                item["title"] = item["title"] or row.get("Title", "").strip()
                item["difficulty"] = item["difficulty"] or row.get("Difficulty", "").title()
                item["topics"].update(
                    topic.strip() for topic in row.get("Topics", "").split(",") if topic.strip()
                )
                company_data = item["companies"].setdefault(company, {})
                company_data["frequency"] = parse_number(row.get("Frequency")) or 0.0
                company_data["window"] = "all"

        if current_dir:
            for row in read_csv(current_dir / "all.csv"):
                url = normalize_url(row.get("URL", ""))
                if not url:
                    continue
                item = problems.setdefault(url, empty_problem(url))
                item["title"] = item["title"] or row.get("Title", "").strip()
                item["difficulty"] = item["difficulty"] or row.get("Difficulty", "").title()
                company_data = item["companies"].setdefault(company, {})
                company_data["frequency"] = parse_number(row.get("Frequency %")) or 0.0
                company_data.setdefault("window", "all")

            for filename, (window, _) in CURRENT_RECENCY_FILES.items():
                for row in read_csv(current_dir / filename):
                    url = normalize_url(row.get("URL", ""))
                    if url in problems and company in problems[url]["companies"]:
                        old = problems[url]["companies"][company].get("window", "all")
                        order = {"all": 0, "6m": 1, "3m": 2, "30d": 3}
                        if order[window] > order[old]:
                            problems[url]["companies"][company]["window"] = window
        elif archive_dir:
            for filename, (window, _) in RECENCY_FILES.items():
                for row in read_csv(archive_dir / filename):
                    url = normalize_url(row.get("Link", ""))
                    if url in problems and company in problems[url]["companies"]:
                        old = problems[url]["companies"][company].get("window", "all")
                        order = {"all": 0, "6m": 1, "3m": 2, "30d": 3}
                        if order[window] > order[old]:
                            problems[url]["companies"][company]["window"] = window

    for url, item in problems.items():
        values = metadata.get(url, {})
        item["id"] = values.get("id", item["id"])
        item["title"] = values.get("title", item["title"])
        item["difficulty"] = values.get("difficulty", item["difficulty"]).title()
        item["acceptance"] = values.get("acceptance")
    return problems


def load_curated_lists(root: Path, problems: dict[str, dict[str, Any]]) -> None:
    for path in sorted((root / "content").glob("*.md")):
        slug = path.stem
        category = ""
        for line in path.read_text(encoding="utf-8").splitlines():
            heading = re.match(r"^##\s+(.+)", line)
            if heading:
                category = heading.group(1).strip()
                continue
            if not line.startswith("|") or "leetcode.com/problems/" not in line:
                continue
            cells = [cell.strip() for cell in line.split("|")[1:-1]]
            if len(cells) < 5 or cells[0].lower() == "problem":
                continue
            title, difficulty, url, pattern, _ = cells[:5]
            url = normalize_url(url)
            if url not in problems:
                continue
            item = problems[url]
            item["curated"].add(slug)
            item["curated_patterns"].extend([category, pattern])
            item["title"] = item["title"] or title
            item["difficulty"] = item["difficulty"] or difficulty


def load_local_ranking(path: Path, problems: dict[str, dict[str, Any]]) -> None:
    by_id = {str(item["id"]): item for item in problems.values() if item["id"]}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"\|\s*#(\d+)\s*\|.*?\bLC\s+(\d+)\s*:", line)
        if not match:
            continue
        rank, problem_id = int(match.group(1)), match.group(2)
        if problem_id in by_id:
            current = by_id[problem_id]["local_rank"]
            by_id[problem_id]["local_rank"] = rank if current is None else min(current, rank)
            cells = [cell.strip().strip("*") for cell in line.split("|")[1:-1]]
            if len(cells) >= 4:
                by_id[problem_id]["local_pattern"] = cells[3]


def load_contest_ratings(path: Path, problems: dict[str, dict[str, Any]]) -> None:
    import json

    ratings = json.loads(path.read_text(encoding="utf-8"))
    by_id = {str(row["ID"]): row for row in ratings if row.get("ID") is not None}
    by_url = {
        normalize_url(f"https://leetcode.com/problems/{row['TitleSlug']}"): row
        for row in ratings
        if row.get("TitleSlug")
    }
    for url, item in problems.items():
        row = by_url.get(url)
        if row is None and item["id"]:
            row = by_id.get(str(item["id"]))
        if row is not None:
            item["contest_rating"] = float(row["Rating"])


def topic_text(item: dict[str, Any]) -> str:
    values = list(item["topics"]) + item["curated_patterns"] + [item["title"]]
    return " ".join(values).lower()


def classify_family(item: dict[str, Any]) -> str:
    text = topic_text(item)
    topic_names = {topic.lower() for topic in item["topics"]}
    title = item["title"].lower()
    preferred = item["local_pattern"].lower()

    def has_word(value: str, word: str) -> bool:
        return bool(re.search(rf"\b{re.escape(word)}\b", value))

    def has_any(value: str, words: list[str]) -> bool:
        return any(has_word(value, word) for word in words)

    if preferred:
        if has_any(preferred, ["random", "randomization", "sampling", "concurrency"]):
            return "Randomized, concurrency, specialized"
        if any(key in preferred for key in ["shortest path", "dijkstra", "bellman", "mst", "euler"]):
            return "Shortest paths, MST, advanced graphs"
        if any(key in preferred for key in ["topological", "union-find", "union find", "dsu", "graph", "bfs", "dfs"]):
            if "grid" in preferred or "matrix" in preferred:
                return "Matrix, grid, geometry"
            return "Graph traversal, topo, union-find"
        if has_any(preferred, ["tree", "bst"]):
            return "Trees, BST"
        if any(key in preferred for key in ["interval", "sweep", "prefix", "range query"]):
            return "Prefix sums, intervals, sweep line"
        if any(key in preferred for key in ["heap", "stream", "ordered set"]):
            return "Heaps, streams, ordered sets"
        if any(key in preferred for key in ["monotonic", "stack", "queue", "deque"]):
            return "Stack, queue, monotonic structures"
        if any(key in preferred for key in ["sliding", "two pointer"]):
            return "Two pointers, sliding window"
        if "binary search" in preferred:
            return "Binary search, selection"
        if "linked list" in preferred:
            return "Linked lists"
        if "trie" in preferred:
            return "Strings, parsing, tries"
        if any(key in preferred for key in ["backtracking", "combinatorial"]):
            return "Backtracking, combinatorial search"
        if "dp" in preferred or "dynamic programming" in preferred:
            if any(key in preferred for key in ["2d", "2-d", "interval", "tree", "string", "matrix", "game", "bitmask"]):
                return "Advanced DP"
            return "1D DP, knapsack"
        if "greedy" in preferred or "sorting" in preferred:
            return "Sorting, greedy"
        if any(key in preferred for key in ["grid", "matrix", "geometry"]):
            return "Matrix, grid, geometry"
        if "bit" in preferred:
            return "Bit manipulation"
        if any(key in preferred for key in ["design", "cache", "iterator"]):
            return "Data-structure design, caches"
        if any(key in preferred for key in ["string", "parsing"]):
            return "Strings, parsing, tries"
        if "math" in preferred:
            return "Math, combinatorics"

    if topic_names.intersection({"randomized", "probability and statistics", "concurrency"}) or has_any(
        text, ["random", "reservoir", "concurrency", "thread", "probability"]
    ):
        return "Randomized, concurrency, specialized"
    if any(
        key in text
        for key in [
            "shortest path",
            "dijkstra",
            "bellman",
            "floyd-warshall",
            "floyd warshall",
            "minimum spanning",
            "eulerian",
        ]
    ):
        return "Shortest paths, MST, advanced graphs"
    if "backtracking" in topic_names:
        return "Backtracking, combinatorial search"
    if topic_names.intersection({"topological sort", "union find", "graph", "graph theory", "strongly connected component"}):
        return "Graph traversal, topo, union-find"
    if topic_names.intersection({"breadth-first search", "depth-first search"}):
        if topic_names.intersection({"matrix", "geometry"}) or has_any(title, ["grid", "matrix", "island", "maze"]):
            return "Matrix, grid, geometry"
        return "Graph traversal, topo, union-find"
    if topic_names.intersection({"binary search tree", "binary tree", "tree"}):
        return "Trees, BST"
    if "trie" in topic_names:
        return "Strings, parsing, tries"
    if topic_names.intersection({"segment tree", "binary indexed tree", "design", "iterator"}) or has_any(title, ["cache", "file system"]):
        return "Data-structure design, caches"
    if topic_names.intersection({"prefix sum", "difference array", "sweep line"}) or has_any(title, ["interval", "intervals", "calendar"]):
        return "Prefix sums, intervals, sweep line"
    if topic_names.intersection({"heap (priority queue)", "data stream", "ordered set"}):
        return "Heaps, streams, ordered sets"
    if topic_names.intersection({"monotonic stack", "monotonic queue", "stack", "queue"}) or "calculator" in title:
        return "Stack, queue, monotonic structures"
    if topic_names.intersection({"sliding window", "two pointers"}):
        return "Two pointers, sliding window"
    if topic_names.intersection({"binary search", "quickselect"}):
        return "Binary search, selection"
    if topic_names.intersection({"linked list", "doubly-linked list"}):
        return "Linked lists"
    if "dynamic programming" in topic_names or "memoization" in topic_names:
        advanced = ["2-d", "2d", "interval", "tree dp", "string dp", "bitmask", "game", "matrix", "digit dp"]
        if any(key in text for key in advanced):
            return "Advanced DP"
        return "1D DP, knapsack"
    if topic_names.intersection({"matrix", "geometry"}):
        return "Matrix, grid, geometry"
    if topic_names.intersection({"greedy", "sorting", "merge sort", "counting sort", "radix sort"}):
        return "Sorting, greedy"
    if topic_names.intersection({"bit manipulation", "bitmask"}):
        return "Bit manipulation"
    if topic_names.intersection({"string matching", "rolling hash", "suffix array", "string"}):
        return "Strings, parsing, tries"
    if topic_names.intersection({"math", "combinatorics", "number theory"}):
        return "Math, combinatorics"
    return "Arrays, hashing, counting"


def score_problem(item: dict[str, Any]) -> float:
    company_values = sorted(
        (COMPANY_WEIGHTS[name] for name in item["companies"] if name in COMPANY_WEIGHTS),
        reverse=True,
    )
    company_score = min(32.0, sum(company_values[:5]))

    recent_score = 0.0
    for company, data in item["companies"].items():
        window = data.get("window", "all")
        recency = {"30d": 10, "3m": 7, "6m": 4, "all": 0}[window]
        multiplier = 1.4 if company in PRIORITY_COMPANIES else 0.7
        recent_score = max(recent_score, recency * multiplier)

    max_frequency = max(
        (data.get("frequency", 0.0) for data in item["companies"].values()),
        default=0.0,
    )
    frequency_score = min(10.0, max_frequency / 10.0)

    curated_score = min(
        28.0,
        sum(CURATED_WEIGHTS.get(name, 2) for name in item["curated"]),
    )

    local_score = 0.0
    if item["local_rank"] is not None:
        local_score = 30.0 * (301 - item["local_rank"]) / 300

    diversity_score = min(9.0, math.log2(1 + len(item["companies"])) * 2.5)
    difficulty_score = 5.0 if item["difficulty"] == "Medium" else 4.0
    return company_score + recent_score + frequency_score + curated_score + local_score + diversity_score + difficulty_score


def complexity_score(item: dict[str, Any]) -> float:
    text = topic_text(item)
    value = 0.0
    if item["acceptance"] is not None:
        value += max(0.0, 60.0 - item["acceptance"]) / 5.0
    for keyword in [
        "topological", "union find", "shortest path", "dijkstra", "monotonic",
        "segment tree", "binary indexed tree", "trie", "bitmask", "sweep line",
        "dynamic programming", "backtracking", "design", "geometry", "random",
    ]:
        if keyword in text:
            value += 1.5
    if item["local_rank"] is not None and item["local_rank"] <= 100:
        value += 3.0
    if item["contest_rating"] is not None:
        value += max(0.0, min(10.0, (item["contest_rating"] - 1400.0) / 100.0))
    return value


def eligible(item: dict[str, Any]) -> bool:
    if item["difficulty"] not in {"Medium", "Hard"}:
        return False
    text = topic_text(item)
    if "database" in text or "shell" in text:
        return False
    slug = item["url"].rstrip("/").rsplit("/", 1)[-1]
    if slug in NON_ALGORITHM_SLUGS:
        return False
    return bool(item["title"] and item["url"] and item["companies"])


def select_by_family(candidates: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    by_family: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in candidates:
        by_family[item["family"]].append(item)
    for values in by_family.values():
        values.sort(key=lambda item: (-item["score"], item["title"]))

    selected: list[dict[str, Any]] = []
    unselected: list[dict[str, Any]] = []
    for family, target in FAMILY_TARGETS.items():
        values = by_family.get(family, [])
        selected.extend(values[:target])
        unselected.extend(values[target:])

    if len(selected) < 1500:
        used = {item["url"] for item in selected}
        extras = sorted(
            (item for item in candidates if item["url"] not in used),
            key=lambda item: (-item["score"], item["title"]),
        )
        selected.extend(extras[: 1500 - len(selected)])
    elif len(selected) > 1500:
        selected.sort(key=lambda item: (-item["score"], item["title"]))
        unselected.extend(selected[1500:])
        selected = selected[:1500]
    return selected, unselected


def enforce_hard_quota(
    selected: list[dict[str, Any]],
    all_candidates: list[dict[str, Any]],
    hard_target: int = 225,
) -> list[dict[str, Any]]:
    selected_urls = {item["url"] for item in selected}
    hard_count = sum(item["difficulty"] == "Hard" for item in selected)

    if hard_count > hard_target:
        outgoing = sorted(
            (item for item in selected if item["difficulty"] == "Hard"),
            key=lambda item: (item["score"], item["title"]),
        )
        incoming_by_family: dict[str, deque[dict[str, Any]]] = {}
        for family in FAMILY_TARGETS:
            incoming = sorted(
                (
                    item for item in all_candidates
                    if item["family"] == family
                    and item["difficulty"] == "Medium"
                    and item["url"] not in selected_urls
                ),
                key=lambda item: (-item["score"], item["title"]),
            )
            incoming_by_family[family] = deque(incoming)

        replacements = hard_count - hard_target
        for old in outgoing:
            if replacements == 0:
                break
            bucket = incoming_by_family[old["family"]]
            if not bucket:
                continue
            new = bucket.popleft()
            selected.remove(old)
            selected.append(new)
            selected_urls.remove(old["url"])
            selected_urls.add(new["url"])
            replacements -= 1
    elif hard_count < hard_target:
        outgoing = sorted(
            (item for item in selected if item["difficulty"] == "Medium"),
            key=lambda item: (item["score"], item["title"]),
        )
        incoming_by_family = {}
        for family in FAMILY_TARGETS:
            incoming = sorted(
                (
                    item for item in all_candidates
                    if item["family"] == family
                    and item["difficulty"] == "Hard"
                    and item["url"] not in selected_urls
                ),
                key=lambda item: (-item["score"], item["title"]),
            )
            incoming_by_family[family] = deque(incoming)

        replacements = hard_target - hard_count
        for old in outgoing:
            if replacements == 0:
                break
            bucket = incoming_by_family[old["family"]]
            if not bucket:
                continue
            new = bucket.popleft()
            selected.remove(old)
            selected.append(new)
            selected_urls.remove(old["url"])
            selected_urls.add(new["url"])
            replacements -= 1
    return selected


def assign_practice_band(selected: list[dict[str, Any]]) -> None:
    medium = sorted(
        (item for item in selected if item["difficulty"] == "Medium"),
        key=lambda item: (-item["complexity"], -item["score"], item["title"]),
    )
    medium_hard_urls = {item["url"] for item in medium[:450]}
    for item in selected:
        if item["difficulty"] == "Hard":
            item["practice_band"] = "Hard"
        elif item["url"] in medium_hard_urls:
            item["practice_band"] = "Medium-hard"
        else:
            item["practice_band"] = "Medium"


def apportion_tiers(family_totals: dict[str, int]) -> dict[str, list[int]]:
    sizes = [size for _, size in TIER_SIZES]
    matrix: dict[str, list[int]] = {}
    fractions: list[tuple[float, str, int]] = []
    row_remaining: dict[str, int] = {}
    column_remaining = sizes.copy()

    for family, total in family_totals.items():
        raw = [total * size / 1500 for size in sizes]
        counts = [math.floor(value) for value in raw]
        matrix[family] = counts
        row_remaining[family] = total - sum(counts)
        for index, value in enumerate(raw):
            fractions.append((value - math.floor(value), family, index))
        for index, count in enumerate(counts):
            column_remaining[index] -= count

    for _, family, index in sorted(fractions, reverse=True):
        if row_remaining[family] and column_remaining[index]:
            matrix[family][index] += 1
            row_remaining[family] -= 1
            column_remaining[index] -= 1

    while any(column_remaining):
        progress = False
        for family in family_totals:
            for index in range(len(sizes)):
                if row_remaining[family] and column_remaining[index]:
                    matrix[family][index] += 1
                    row_remaining[family] -= 1
                    column_remaining[index] -= 1
                    progress = True
        if not progress:
            raise RuntimeError("Could not apportion tier quotas")
    return matrix


def assign_tiers(selected: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    by_family: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in selected:
        by_family[item["family"]].append(item)
    for values in by_family.values():
        values.sort(key=lambda item: (-item["score"], item["title"]))
    matrix = apportion_tiers({family: len(values) for family, values in by_family.items()})

    tiers: dict[str, list[dict[str, Any]]] = {name: [] for name, _ in TIER_SIZES}
    for family, counts in matrix.items():
        values = by_family[family]
        offset = 0
        for (tier_name, _), count in zip(TIER_SIZES, counts):
            chunk = values[offset : offset + count]
            for item in chunk:
                item["tier"] = tier_name
            tiers[tier_name].extend(chunk)
            offset += count
    return tiers


def mixed_order(
    items: list[dict[str, Any]],
    prior_tail: list[dict[str, Any]] | None = None,
) -> list[dict[str, Any]]:
    buckets: dict[str, deque[dict[str, Any]]] = defaultdict(deque)
    for family in FAMILY_TARGETS:
        values = sorted(
            (item for item in items if item["family"] == family),
            key=lambda item: (-item["score"], item["title"]),
        )
        buckets[family] = deque(values)

    output: list[dict[str, Any]] = []
    prior_tail = (prior_tail or [])[-9:]
    hard_total = sum(item["practice_band"] == "Hard" for item in items)
    hard_used = 0
    group_index = 0
    while len(output) < len(items):
        chosen: dict[str, Any] | None = None
        chosen_family = ""
        context = prior_tail + output
        remaining_families = [family for family, values in buckets.items() if values]
        hard_due = hard_used < ((len(output) + 1) * hard_total) // len(items)
        candidates: dict[str, dict[str, Any]] = {}
        for family in remaining_families:
            candidate = next(
                (
                    item
                    for item in buckets[family]
                    if (item["practice_band"] == "Hard") == hard_due
                ),
                None,
            )
            if candidate is not None:
                candidates[family] = candidate
        if not candidates:
            candidates = {family: buckets[family][0] for family in remaining_families}
        can_change_family = bool(context) and any(
            family != context[-1]["family"] for family in candidates
        )
        for shift in range(len(ROTATION_GROUPS)):
            group = ROTATION_GROUPS[(group_index + shift) % len(ROTATION_GROUPS)]
            options = [family for family in group if family in candidates]
            if can_change_family:
                options = [family for family in options if family != context[-1]["family"]]
            if options:
                chosen_family = max(options, key=lambda family: candidates[family]["score"])
                chosen = candidates[chosen_family]
                buckets[chosen_family].remove(chosen)
                hard_used += chosen["practice_band"] == "Hard"
                group_index = (group_index + shift + 1) % len(ROTATION_GROUPS)
                break
        if chosen is None:
            remaining = [family for family, values in buckets.items() if values]
            if not remaining:
                break
            chosen_family = max(remaining, key=lambda family: buckets[family][0]["score"])
            chosen = buckets[chosen_family].popleft()
            hard_used += chosen["practice_band"] == "Hard"
        output.append(chosen)
    return output


def recency_summary(item: dict[str, Any]) -> str:
    order = {"30d": 0, "3m": 1, "6m": 2, "all": 3}
    values = [
        f"{company}:{data['window']}"
        for company, data in sorted(
            item["companies"].items(),
            key=lambda pair: (order[pair[1].get("window", "all")], -COMPANY_WEIGHTS.get(pair[0], 0), pair[0]),
        )
        if data.get("window", "all") != "all"
    ]
    return "; ".join(values[:6])


def company_summary(item: dict[str, Any]) -> str:
    ordered = sorted(
        item["companies"],
        key=lambda name: (
            0 if name in PRIORITY_COMPANIES else 1,
            -COMPANY_WEIGHTS.get(name, 0),
            name,
        ),
    )
    shown = ordered[:5]
    suffix = f" +{len(ordered) - len(shown)}" if len(ordered) > len(shown) else ""
    return ", ".join(shown) + suffix


def why_summary(item: dict[str, Any]) -> str:
    values: list[str] = []
    priority = [name for name in PRIORITY_COMPANIES if name in item["companies"]]
    if priority:
        values.append("/".join(priority) + " associated")
    recent = recency_summary(item)
    if recent:
        values.append("recent tag window")
    if item["local_rank"] is not None:
        values.append(f"Google L5 list #{item['local_rank']}")
    if item["curated"]:
        values.append(f"{len(item['curated'])} curated list{'s' if len(item['curated']) != 1 else ''}")
    if len(item["companies"]) >= 5:
        values.append(f"{len(item['companies'])} target-company tags")
    return "; ".join(values) or "company tag + pattern coverage"


def write_csv(path: Path, ordered: list[dict[str, Any]]) -> None:
    fields = [
        "rank", "tier", "leetcode_id", "title", "url", "official_difficulty",
        "practice_band", "primary_family", "topics", "companies", "company_count",
        "recent_windows", "max_frequency", "acceptance_percent", "curated_lists",
        "local_google_rank", "contest_rating", "evidence", "why_included",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for rank, item in enumerate(ordered, 1):
            writer.writerow({
                "rank": rank,
                "tier": item["tier"],
                "leetcode_id": item["id"],
                "title": item["title"],
                "url": item["url"],
                "official_difficulty": item["difficulty"],
                "practice_band": item["practice_band"],
                "primary_family": item["family"],
                "topics": "; ".join(sorted(item["topics"])),
                "companies": "; ".join(sorted(item["companies"])),
                "company_count": len(item["companies"]),
                "recent_windows": recency_summary(item),
                "max_frequency": max(
                    (data.get("frequency", 0.0) for data in item["companies"].values()),
                    default=0.0,
                ),
                "acceptance_percent": item["acceptance"] if item["acceptance"] is not None else "",
                "curated_lists": "; ".join(sorted(item["curated"])),
                "local_google_rank": item["local_rank"] or "",
                "contest_rating": round(item["contest_rating"], 1) if item["contest_rating"] is not None else "",
                "evidence": "Community company-tag snapshots; curated-list cross-check",
                "why_included": why_summary(item),
            })


def write_markdown(path: Path, ordered: list[dict[str, Any]]) -> None:
    by_tier: dict[str, list[tuple[int, dict[str, Any]]]] = defaultdict(list)
    for rank, item in enumerate(ordered, 1):
        by_tier[item["tier"]].append((rank, item))

    lines = [
        "# 1,500 coding problems: ranked mixed backlog",
        "",
        "Work downward, but re-solve misses between new problems. The order inside each tier is deliberately mixed by problem family.",
        "",
        "This is a backlog, not a claim that all 1,500 are equally necessary. In four to six months, finishing the first 400–600 with repeats and timed practice is stronger than touching all 1,500 once.",
        "",
        "## Tiers",
        "",
        "- **Must solve (1–250):** canonical patterns, strong transfer value, and the best target-company signals.",
        "- **Strong priority (251–600):** important variants and harder follow-ups.",
        "- **Breadth builder (601–1050):** expands pattern and implementation coverage.",
        "- **Useful if time (1051–1350):** narrower variants or weaker company evidence.",
        "- **Meh / optional (1351–1500):** redundant, specialized, contest-like, or weakly sourced compared with earlier choices.",
        "",
        "**Difficulty:** LeetCode's official label is kept in the CSV. `Medium-hard` is a practice label for Medium problems with harder modeling, state, proof, or implementation.",
        "",
        "**Company tags:** read these as *associated with* or *reported for*, not as verified predictions. The source data is community-maintained and ultimately derived from LeetCode company tags.",
        "",
        "The filterable version is [`master-1500.csv`](master-1500.csv). Method and sources are in [`master-1500-method.md`](master-1500-method.md).",
        "",
    ]

    for tier_name, _ in TIER_SIZES:
        lines.extend([
            f"## {tier_name}",
            "",
            "| Rank | Problem | Practice | Primary type | Company signal | Why here |",
            "|---:|---|---|---|---|---|",
        ])
        for rank, item in by_tier[tier_name]:
            problem = f"[{item['title']}]({item['url']})"
            if item["id"]:
                problem = f"LC {item['id']}: {problem}"
            lines.append(
                f"| {rank} | {problem} | {item['practice_band']} | {item['family']} | "
                f"{company_summary(item)} | {why_summary(item)} |"
            )
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", type=Path, required=True, help="liquidslr company-tag snapshot")
    parser.add_argument("--current", type=Path, required=True, help="May 2026 company-tag mirror with IDs")
    parser.add_argument("--curated", type=Path, required=True, help="curated roadmap repository")
    parser.add_argument("--ratings", type=Path, required=True, help="Zerotrac data.json")
    parser.add_argument("--local-ranking", type=Path, default=Path("notes/likely-problems.md"))
    parser.add_argument("--output-csv", type=Path, default=Path("notes/master-1500.csv"))
    parser.add_argument("--output-md", type=Path, default=Path("notes/MASTER_1500.md"))
    args = parser.parse_args()

    metadata = load_global_metadata(args.current)
    problems = load_company_data(args.archive, args.current, metadata)
    load_curated_lists(args.curated, problems)
    load_local_ranking(args.local_ranking, problems)
    load_contest_ratings(args.ratings, problems)

    candidates = [item for item in problems.values() if eligible(item)]
    for item in candidates:
        item["family"] = classify_family(item)
        item["score"] = score_problem(item)
        item["complexity"] = complexity_score(item)

    selected, _ = select_by_family(candidates)
    selected = enforce_hard_quota(selected, candidates)
    assign_practice_band(selected)
    tiers = assign_tiers(selected)

    ordered: list[dict[str, Any]] = []
    for tier_name, expected_size in TIER_SIZES:
        tier_items = mixed_order(tiers[tier_name], ordered[-9:])
        if len(tier_items) != expected_size:
            raise RuntimeError(f"{tier_name}: expected {expected_size}, got {len(tier_items)}")
        ordered.extend(tier_items)

    if len({item["url"] for item in ordered}) != 1500:
        raise RuntimeError("Output does not contain 1,500 unique problems")

    write_csv(args.output_csv, ordered)
    write_markdown(args.output_md, ordered)

    print(f"candidates={len(candidates)} selected={len(ordered)}")
    print("tiers=" + ", ".join(f"{name}:{size}" for name, size in TIER_SIZES))
    print("practice=" + ", ".join(
        f"{band}:{sum(item['practice_band'] == band for item in ordered)}"
        for band in ["Medium", "Medium-hard", "Hard"]
    ))
    print("families=" + ", ".join(
        f"{family}:{sum(item['family'] == family for item in ordered)}"
        for family in FAMILY_TARGETS
    ))


if __name__ == "__main__":
    main()
