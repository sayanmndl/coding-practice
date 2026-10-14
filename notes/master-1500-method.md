# Master 1,500: method and sources

## What this list is

The master list is a ranked backlog of 1,500 unique Medium, Medium-hard, and Hard problems. It favors Google and Waymo, then Meta and LinkedIn, then other top technology, AI, infrastructure, mobility, and trading companies.

It is not a prediction that these exact questions will appear. Company tags are noisy, copied between datasets, and affected by self-reporting and LeetCode access.

## Tiers

| Tier | Size | Meaning |
|---|---:|---|
| Must solve | 250 | Canonical patterns, strong transfer value, strongest company and curated-list signals |
| Strong priority | 350 | Important variants and harder follow-ups |
| Breadth builder | 450 | Wider pattern and implementation coverage |
| Useful if time | 300 | Narrower variants or weaker evidence |
| Meh / optional | 150 | Redundant, specialized, contest-like, or weakly sourced relative to earlier problems |

The order inside each tier is mixed across problem families. It is a practice sequence, not a claim that rank 87 has a measurable interview probability above rank 88.

## Inputs

1. [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions), snapshot commit `e095c259cfd036e3ddb6886e84d7075c2faac477` from 2026-08-16. Used for LeetCode IDs, readable acceptance percentages, company tags, frequency fields, and 30-day/3-month/6-month windows.
2. [liquidslr/leetcode-company-wise-problems](https://github.com/liquidslr/leetcode-company-wise-problems), snapshot commit `03850eb5d16892514491cf1381c32ec0330a2719` from 2026-08-16. Used for topic enrichment and as a fallback when a company is absent from the primary snapshot.
3. [sumitsingh4411/faang](https://github.com/sumitsingh4411/faang), snapshot commit `fa161dba94cb9991ebedd12b13633db2ce7d0563` from 2026-07-25. Used only for membership in public curated sets such as Top Interview 150, NeetCode 150/250, Grind 75/169, Blind 75, and company top lists.
4. [zerotrac/leetcode_problem_rating](https://github.com/zerotrac/leetcode_problem_rating), snapshot commit `ef8c9e3c21f8e5375206681f66317e61a990c142` from 2026-10-10. Used as one input for the derived Medium-hard label. Its contest rating is an estimate, not an official LeetCode difficulty.
5. [`likely-problems.md`](likely-problems.md), the existing Google L5/Senior list in this repository. Its first 300 ranks provide a Google-specific transfer and follow-up signal.
6. [LeetCode's current problem catalog](https://leetcode.com/problemset/), checked on 2026-10-14. Its Database, Pandas, JavaScript, and Shell categories provide the exclusions in `tools/non_algorithm_slugs.txt`; concurrency problems remain eligible.

[LeetCode's description of company grouping](https://support.leetcode.com/hc/en-us/articles/360011985113-How-does-grouping-questions-by-company-work) says the tags are based on user interview reports. They are not employer-confirmed disclosures.

No problem statements or solutions are copied. The output contains titles, links, factual metadata, and derived ranking labels. The two community company-tag snapshots do not declare a data-redistribution license, so they are attributed here and are rebuild inputs rather than vendored copies.

## Ranking signals

- Google and Waymo association receives the largest company weight.
- Meta and LinkedIn are next.
- Recent tag windows outrank all-time-only tags.
- Repeated appearance across target companies helps, but the contribution is capped.
- Canonical curated-list membership and the existing Google L5 ranking help identify transferable problems.
- Difficulty fit favors Medium and Medium-hard work while retaining transferable Hards.
- Exact LeetCode URLs are deduplicated.
- SQL/database, Pandas, JavaScript-only, and shell problems are excluded. Concurrency problems remain eligible as a specialized coding type.

The script uses broad score bands internally. The resulting rank is an ordering tool, not a probability estimate.

## Difficulty

- **Medium** and **Hard** preserve LeetCode's official difficulty in the CSV.
- **Medium-hard** is a derived practice label, not an official LeetCode label. It identifies Medium problems with lower acceptance, advanced topics, difficult state/modeling, or strong senior-level follow-up value.
- The final mix is 825 Medium, 450 Medium-hard, and 225 Hard.
- Easy problems are excluded, matching the practice plan. Review a missing foundation directly, then use it inside a Medium problem.

## Pattern coverage

Each problem has one primary family for scheduling and may retain several source topic tags. The 1,500 slots are distributed across 20 families, then mixed inside every tier so adjacent rows rarely use the same main idea.

## Rebuild

Clone the three source repositories, then run:

```bash
python3 tools/build_master_1500.py \
  --archive /path/to/leetcode-company-wise-problems \
  --current /path/to/leetcode-companywise-interview-questions \
  --curated /path/to/faang \
  --ratings /path/to/leetcode_problem_rating/data.json
```

The command rewrites:

- `notes/master-1500.csv`
- `notes/MASTER_1500.md`

## Limits

- Company associations are community-maintained snapshots, not employer-confirmed question banks.
- A frequency value is meaningful only inside its source dataset. It is not a probability that a company will ask the problem.
- Waymo has far fewer public tags than Google, Meta, or Amazon. The ranking boosts Waymo-tagged problems but does not infer Waymo relevance from a Google tag.
- Curated roadmaps are used as cross-checks, not proof of company usage.
- New questions and renamed problems will require a future rebuild.
