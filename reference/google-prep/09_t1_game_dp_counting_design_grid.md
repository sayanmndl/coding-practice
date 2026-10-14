# Tier 1 — Game DP, inversion counting, design classes, grid paths

Four Tier 1 must-dos: **LC 1406** Stone Game III (game DP), **LC 315** Count of Smaller Numbers After Self (+493), **LC 981** Time Based Key-Value Store (+1146), and **LC 2812** Find the Safest Path in a Grid (reported in a Dec 2025 Google L5 onsite).
Every solution was tested in a scratch file with fixed asserts plus randomized checks against a brute force (or memo vs. bottom-up) where that applies.

## 1. LC 1406 — Stone Game III (game / minimax DP) — Hard — Tier 1 ✅ tested
**Prompt (as asked):** Stones in a row with integer values (which can be negative). Alice and Bob alternate turns, starting with Alice. On each turn a player takes 1, 2, or 3 stones from the **front**. Both play optimally. Return `"Alice"`, `"Bob"`, or `"Tie"`.
Example: `[1,2,3,7]` → `"Bob"`. Example: `[1,2,3,-9]` → `"Alice"` (she takes all three positives and leaves Bob the -9).

**Clarify:** Can values be negative? (yes, so taking more isn't always better). Must a player take at least 1 stone? (yes). n up to 5e4? (yes → O(n)). Do we need the actual scores? (no, only who wins; the difference is enough).

**Approach:** Brute force: a minimax game tree with branching factor 3, O(3ⁿ). Key insight: it's zero-sum, so track the **score difference** (current player minus opponent). The state is just the index `i`, and whoever moves faces the same subproblem.
Recurrence: `dp[i] = max over k∈{1,2,3} of (sum(stones[i:i+k]) − dp[i+k])`, with `dp[n] = 0`. Answer: the sign of `dp[0]`. **O(n) time.** The bottom-up version can use O(1) space by keeping only `dp[i+1..i+3]`.
```python
from functools import lru_cache

def stone_game_iii_memo(stones: List[int]) -> str:   # O(n) time, O(n) space
    n = len(stones)
    @lru_cache(maxsize=None)
    def best(i: int) -> int:          # max (me - opponent) starting at index i
        if i >= n:
            return 0
        res, take = float("-inf"), 0
        for k in range(i, min(i + 3, n)):
            take += stones[k]
            res = max(res, take - best(k + 1))
        return res
    d = best(0)
    return "Alice" if d > 0 else "Bob" if d < 0 else "Tie"

def stone_game_iii(stones: List[int]) -> str:        # O(n) time, O(n) space
    n = len(stones)
    dp = [0] * (n + 3)                # dp[i] = best diff from i; dp[n..] = 0
    for i in range(n - 1, -1, -1):
        take, dp[i] = 0, float("-inf")
        for k in range(i, min(i + 3, n)):
            take += stones[k]
            dp[i] = max(dp[i], take - dp[k + 1])
    return "Alice" if dp[0] > 0 else "Bob" if dp[0] < 0 else "Tie"
```
**Dry run:** `[1,2,3,7]`. dp[3] = 7. dp[2] = max(3−7, 3+7−0) = 10. dp[1] = max(2−10, 5−7, 12−0) = 12. dp[0] = max(1−12, 3−10, 6−7) = **−1** → `"Bob"`.

**Edge cases & tests:**
- A single positive, negative, or zero stone; all negatives (both players are forced to take); n < 3, where the k-loop must clamp at n.
- `assert f([1,2,3,7]) == "Bob"`, `([1,2,3,-9]) == "Alice"`, `([1,2,3,6]) == "Tie"`, `([5]) == "Alice"`, `([-1]) == "Bob"`, `([0]) == "Tie"`, `([-1,-2,-3]) == "Tie"`, plus 300 random arrays where memo == bottom-up.
- Memo recursion depth is about n, which hits Python's limit at 5e4. Say this out loud and prefer bottom-up.

**Follow-ups:**
- *Return Alice's actual score?* Total = A + B and diff = A − B, so A = (total + dp[0]) / 2.
- *Take up to M stones?* The same DP with an O(nM) loop. Use a sliding window of suffix sums for the take amount.
- *Stone Game I/II?* Game I (take from either end) is an interval DP `dp[i][j]`. Game II adds the state `(i, M)`. Same idea: maximize the difference.

**Pattern hook:** two optimal players, zero-sum → `dp[state] = max(gain − dp[next_state])`. The score difference collapses the minimax.

## 2. LC 315 — Count of Smaller Numbers After Self (merge sort / Fenwick tree) — Hard — Tier 1 ✅ tested
**Prompt (as asked):** For each `nums[i]`, return how many elements to its **right** are strictly smaller.
Example: `[5,2,6,1]` → `[2,1,1,0]`.

**Clarify:** Duplicates? (yes, strictly smaller only). Negatives or large values? (yes → compress coordinates). n up to 1e5? (yes → O(n log n)). Empty input? (return `[]`).

**Approach:** Brute force is O(n²). **(A) Merge sort:** sort *indices* by value. While merging, every right-half element placed before left element `x` is smaller and was originally to x's right, so add `j − mid` to `res[x]`. **(B) BIT:** scan right to left. Map values to ranks 1..m. Answer = `prefix(rank−1)`, then `add(rank)`. Both are **O(n log n) time, O(n) space.**
```python
def count_smaller_ms(nums: List[int]) -> List[int]:  # O(n log n)
    n = len(nums); res = [0] * n; idx = list(range(n))
    def sort(lo: int, hi: int) -> None:      # sorts idx[lo:hi] by value
        if hi - lo <= 1: return
        mid = (lo + hi) // 2
        sort(lo, mid); sort(mid, hi)
        merged, j = [], mid
        for i in range(lo, mid):
            while j < hi and nums[idx[j]] < nums[idx[i]]:
                merged.append(idx[j]); j += 1
            res[idx[i]] += j - mid           # right-half elems smaller than it
            merged.append(idx[i])
        merged.extend(idx[j:hi])
        idx[lo:hi] = merged
    sort(0, n)
    return res

def count_smaller_bit(nums: List[int]) -> List[int]:  # O(n log n)
    ranks = {v: i + 1 for i, v in enumerate(sorted(set(nums)))}
    tree = [0] * (len(ranks) + 1)
    def add(i: int) -> None:
        while i < len(tree): tree[i] += 1; i += i & -i
    def query(i: int) -> int:                # count of ranks <= i
        s = 0
        while i > 0: s += tree[i]; i -= i & -i
        return s
    res = []
    for v in reversed(nums):
        res.append(query(ranks[v] - 1)); add(ranks[v])
    return res[::-1]
```
**Dry run (BIT):** ranks are 1→1, 2→2, 5→3, 6→4. Scan 1: q(0)=0. Scan 6: q(3)=1. Scan 2: q(1)=1. Scan 5: q(2)=2. Reversed → `[2,1,1,0]`.

**Edge cases & tests:** empty, single element, duplicates (strict `<`, so equal values aren't counted), sorted and reverse-sorted input.
`assert f([5,2,6,1]) == [2,1,1,0]`, `([-1,-1]) == [0,0]`, `([]) == []`, `([1,2,3]) == [0,0,0]`, `([3,2,1]) == [2,1,0]`, plus 300 random arrays vs. the O(n²) brute force for each version.

**Follow-ups:**
- *Streaming (count smaller among those seen so far)?* BIT handles this online. If the value range is unknown, use a balanced BST/order-statistic tree or a dynamic segment tree.
- *Total inversions only?* Sum the result, or count during the merge.
- *Doesn't fit in memory?* External merge sort with counts carried per chunk, or a BIT over value buckets.

**Pattern hook:** "how many to the right are smaller/larger" → inversion counting: merge sort on indices, or a BIT over ranks.

**Sibling: LC 493 Reverse Pairs** (count `i<j` with `nums[i] > 2·nums[j]`). The condition isn't the merge order, so count in a **separate two-pointer pass** over the two sorted halves *before* merging. The pointer `j` only moves forward because L is sorted. O(n log n). (Python ints don't overflow; in Java/C++ use `long` for `2*x`.)
```python
def reverse_pairs(nums: List[int]) -> int:
    def sort(a: List[int]) -> Tuple[List[int], int]:
        if len(a) <= 1: return a, 0
        L, cl = sort(a[:len(a)//2]); R, cr = sort(a[len(a)//2:])
        cnt, j = cl + cr, 0
        for x in L:
            while j < len(R) and x > 2 * R[j]: j += 1
            cnt += j
        return sorted(L + R), cnt      # Timsort merges two runs in O(n)
    return sort(nums)[1]
```
Tests: `[1,3,2,3,1]→2`, `[2,4,3,5,1]→3`, `[]→0`, `[-5,-5]→1`, plus 300 random vs. brute force.

## 3. LC 981 — Time Based Key-Value Store (design + binary search) — Medium — Tier 1 ✅ tested
**Prompt (as asked):** Design `TimeMap` with `set(key, value, timestamp)` and `get(key, timestamp)`. `get` returns the value whose timestamp is the largest one ≤ `timestamp`, or `""` if there isn't one.
Example: `set("foo","bar",1)`, `get("foo",3)` → `"bar"`, `set("foo","bar2",4)`, `get("foo",4)` → `"bar2"`, `get("foo",0)` → `""`.

**Clarify:** Are timestamps strictly increasing per key? (yes, per LC → append keeps lists sorted). Same key and timestamp twice? (not in LC; otherwise overwrite). Read/write ratio? (reads dominate). Thread safety? (single-threaded for now).

**Approach:** Brute force: store all (t, v) pairs and scan linearly on get, O(n). Key insight: timestamps arrive sorted, so each key gets an append-only sorted list. Then `get` = `bisect_right(ts, t) − 1` (the floor). **set O(1), get O(log n), O(total) space.** Parallel lists avoid tuple-comparison tricks.
```python
from bisect import bisect_right
from collections import defaultdict

class TimeMap:
    def __init__(self) -> None:
        self.times: Dict[str, List[int]] = defaultdict(list)
        self.vals: Dict[str, List[str]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:   # O(1)
        self.times[key].append(timestamp)    # increasing -> stays sorted
        self.vals[key].append(value)

    def get(self, key: str, timestamp: int) -> str:                # O(log n)
        ts = self.times.get(key)
        if not ts:
            return ""
        i = bisect_right(ts, timestamp) - 1  # last ts <= timestamp
        return self.vals[key][i] if i >= 0 else ""
```
**Dry run:** ts["foo"] = [1,4]. get(3): bisect_right = 1 → i=0 → "bar". get(0): bisect_right = 0 → i=−1 → "". get(5): i=1 → "bar2".

**Edge cases & tests:** missing key (using `.get` avoids creating an empty defaultdict entry), query before the first timestamp, an exact match, a query after the last timestamp.
`assert tm.get("foo",1)=="bar"`, `get("foo",3)=="bar"`, `get("foo",4)=="bar2"`, `get("foo",5)=="bar2"`, `get("foo",0)==""`, `get("missing",10)==""`.

**Follow-ups:**
- *Out-of-order timestamps?* Use `sortedcontainers.SortedList`/`SortedDict` per key (O(log n) insert), or insort (O(n) insert).
- *Memory bound / TTL?* Keep a per-key deque and evict old versions below a watermark (like MVCC garbage collection).
- *Distributed / huge scale?* Shard by key. Each shard is an LSM tree with key+timestamp as the sort key (the Bigtable model: cells are versioned by timestamp). The read is a floor seek.
- *Concurrency?* Per-key locks, or single-writer per shard.

**Pattern hook:** "value as of time t" / versioned reads → an append-only sorted list per key plus a floor binary search.

**Sibling: LC 1146 Snapshot Array.** Copying the array on every `snap` costs O(n) per snap. Instead, each index keeps a history of `(snap_id, val)` pairs, overwriting the last entry if it's from the same snap id. `get(i, s)` = floor search for snap_id ≤ s. A `(-1, 0)` sentinel makes unset values read as 0. set/snap O(1), get O(log k).
```python
class SnapshotArray:
    def __init__(self, length: int) -> None:
        self.hist = [[(-1, 0)] for _ in range(length)]
        self.snap_id = 0
    def set(self, index: int, val: int) -> None:
        h = self.hist[index]
        if h[-1][0] == self.snap_id: h[-1] = (self.snap_id, val)
        else: h.append((self.snap_id, val))
    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1
    def get(self, index: int, snap_id: int) -> int:
        h = self.hist[index]
        return h[bisect_right(h, (snap_id, float("inf"))) - 1][1]
```
Tests: set(0,5), snap→0, set(0,6), get(0,0)==5, get(1,0)==0, multiple sets within one snap keep the last value, unchanged across empty snaps (8 asserts).

## 4. LC 2812 — Find the Safest Path in a Grid (multi-source BFS + max-min path) — Medium — Tier 1 ✅ tested
**Prompt (as asked):** n×n grid, where 1 = thief. A path's *safeness* is the min Manhattan distance from any cell on it to any thief. Moving 4-directionally from (0,0) to (n−1,n−1), return the max safeness. (Reported in a Dec 2025 Google L5 onsite.)
Example: `[[0,0,1],[0,0,0],[0,0,0]]` → `2`. Example: `[[1,0,0],[0,0,0],[0,0,1]]` → `0`.

**Clarify:** Is there at least one thief? (yes). Can start or end be a thief? (yes → answer 0). Is Manhattan distance the same as BFS steps here? (yes: no obstacles, 4-dir). n ≤ 400? (yes → n² = 160k cells).

**Approach:** Brute force: for each cell, scan every thief (O(n⁴)), then enumerate paths. Step 1: **multi-source BFS** from all thieves gives `dist[r][c]` in O(n²). Step 2: maximize the bottleneck (min over the path).
- **(A) Binary search + BFS:** "is there a path using only cells with dist ≥ k?" is monotone in k. Search k in [0, min(dist[start], dist[end])]. **O(n² log n).**
- **(B) Dijkstra-style max-heap:** pop the cell with the largest bottleneck. The new value is `min(s, dist[nbr])`, which never increases along a path, so the first pop of the target is optimal. **O(n² log n).** (Option C: union-find, adding cells by dist descending until start and end connect.)
```python
DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

def thief_dist(grid: List[List[int]]) -> List[List[int]]:   # O(n^2)
    n = len(grid); dist = [[-1] * n for _ in range(n)]
    q = deque((r, c) for r in range(n) for c in range(n) if grid[r][c])
    for r, c in q: dist[r][c] = 0
    while q:
        r, c = q.popleft()
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1; q.append((nr, nc))
    return dist

def safest_dijkstra(grid: List[List[int]]) -> int:          # O(n^2 log n)
    n = len(grid); dist = thief_dist(grid)
    best = [[-1] * n for _ in range(n)]
    best[0][0] = dist[0][0]
    heap = [(-dist[0][0], 0, 0)]                # max-heap on bottleneck
    while heap:
        neg, r, c = heapq.heappop(heap); s = -neg
        if (r, c) == (n - 1, n - 1): return s
        if s < best[r][c]: continue             # stale entry
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                ns = min(s, dist[nr][nc])
                if ns > best[nr][nc]:
                    best[nr][nc] = ns; heapq.heappush(heap, (-ns, nr, nc))
    return 0
```
```python
def safest_binsearch(grid: List[List[int]]) -> int:         # O(n^2 log n)
    n = len(grid); dist = thief_dist(grid)
    def reachable(k: int) -> bool:              # path through cells with dist >= k?
        if dist[0][0] < k: return False
        seen, q = {(0, 0)}, deque([(0, 0)])
        while q:
            r, c = q.popleft()
            if (r, c) == (n - 1, n - 1): return True
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if (0 <= nr < n and 0 <= nc < n and (nr, nc) not in seen
                        and dist[nr][nc] >= k):
                    seen.add((nr, nc)); q.append((nr, nc))
        return False
    lo, hi = 0, min(dist[0][0], dist[n - 1][n - 1])   # reachable(0) always True
    while lo < hi:
        mid = (lo + hi + 1) // 2                # upper mid: searching for last True
        if reachable(mid): lo = mid
        else: hi = mid - 1
    return lo
```
**Dry run:** `[[0,0,1],[0,0,0],[0,0,0]]`. dist rows are `[2,1,0]`, `[3,2,1]`, `[4,3,2]`. The path down the left column then along the bottom has min(2,3,4,3,2) = **2**. Binary search: hi = min(2,2) = 2, and reachable(2) is True → 2.

**Edge cases & tests:** a 1×1 grid with a thief → 0, a thief on start or end → 0, an all-thief grid, a thief adjacent to the start.
`assert f([[1,0,0],[0,0,0],[0,0,1]]) == 0`, `f([[0,0,1],[0,0,0],[0,0,0]]) == 2`, `f([[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]) == 2`, `f([[1]]) == 0`, `f([[0,1],[0,0]]) == 1`, `f([[1,1],[1,1]]) == 0`, plus 200 random grids (n ≤ 4) per version vs. an exhaustive simple-path DFS.

**Follow-ups:**
- *Which is better?* Dijkstra makes one pass with early exit. Binary search is simpler to prove correct and reuses plain BFS. Union-find (sort cells by dist descending, union until start ~ end) is O(n² log n) for the sort, or O(n² α) with bucket sort since dist ≤ 2n.
- *Euclidean distance or obstacles?* BFS no longer equals the metric. Use multi-source Dijkstra for weighted distances. With obstacles, BFS respects the walls (if the problem defines distance that way).
- *Return the path itself?* Keep a parent pointer on each heap relaxation.
- *Huge grid / thieves move?* Tile the grid. For moving thieves, add a time dimension (as in LC 2258 Escape the Spreading Fire), binary searching on wait time.

**Pattern hook:** "maximize the minimum along a path" → bottleneck path: binary search on the answer + BFS, a max-heap Dijkstra, or union-find by descending weight. "Distance to nearest X" → multi-source BFS.
