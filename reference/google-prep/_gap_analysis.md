# Google L5 DS&A gap analysis (prepared 2026-10-08)

## (a) Sources

| Source | Date | What I used |
|---|---|---|
| snehasishroy/leetcode-companywise-interview-questions, `google/{thirty-days,three-months,six-months,all}.csv` (raw CSV) | Data "as of 12 July 2026", committed 2026-08-15 | The main frequency signal: 201 problems in 30d, 452 in 3m, 784 in 6m |
| liquidslr/leetcode-company-wise-problems, `Google/{1. Thirty Days … 5. All}.csv` (raw CSV) | File last committed 2026-08-16 | Cross-check, plus the topic tags |
| LeetCode Discuss post "Google 2026 interviews: 8 LeetCode problems confirmed sighted" (/discuss/post/8546037) | 2026 | **Search snippet only** (page returns 403). Names LC 200, 416, 174, 410, 128, 346, 315, 2188 |
| codingkaro.in Google interview-experience digest (mirrors LC Discuss) | Dec 2025 entries | L5 Bangalore: "Find the Safest Path in a Grid" (=2812). L5 BLR: 2D prefix sum on grid. L4: merge intervals, RPC timeout detection, playlist shuffler. L3: min-security path, event timeout. Dec 2025: Subarray Sum Equals K (560) |
| hellointerview.com Google L5 guide | 2026 | Named L5 questions: car rental optimisation, LC 56, 359, 2402, template substitution with cycle detection |
| prachub.com Google SWE guide | 2026 | Rental fleet assignment, sharded login logs, min rooms |
| Search snippets (Blind, LC Discuss phone-screen posts) | 2025–26 | Prefix-count binary search, root that makes a binary tree, "whole class to implement, algorithm buried in one method" |

**What I could not verify.** LeetCode Discuss and Blind pages return 403, so I saw only search snippets of individual reports. LeetCode's frequency field comes in 12.5% buckets, so many problems tie. The tag lists are also polluted by generic popularity: SQL/JS problems and Two Sum appear, so they reflect who tags problems, not Google's real question bank. Google mostly asks original or disguised problems. Treat LC numbers as **pattern proxies**, not likely verbatim questions.

**How I ranked.** I built a recency-weighted composite: 3×(30d) + 2×(3m) + 1×(6m) frequency, summed over both repos, with SQL/JS problems dropped. "Top-50" and "Top-100" below refer to this composite. Within a frequency bucket, the order comes from the composite, not from LeetCode.

## (b) Coverage summary

| Slice | COVERED | VARIANT | Covered + variant | MISSING |
|---|---|---|---|---|
| Top-50 composite | 12 | 12 | **48%** | 26 (≈14 of them trivial easies) |
| Top-100 composite | 23 | 26 | **49%** | 51 (≈25 trivial easies) |

If you leave out trivial easies (Two Sum, Palindrome Number, Contains Duplicate, Merge Strings Alternately, etc.), coverage of the *non-trivial* top-100 is about **65%**.

The coverage is skewed. The inventory is strong on Google's "original-style" problems: design classes, intervals, graphs (BFS, Dijkstra, topological sort, DSU), tries and parsing. It is weak on the high-frequency classic array/string/DP canon that dominates the tag lists.

Covered (top-100): 4, 20, 21, 410, 200, 875, 33, 51, 146, 22, 424, 198, 17, 167, 1944, 994, 322, 295, 162, 394, 56, 239, 253.
Variants: 3 (424/76/340), 15 and 11 (167, weak), 242/49/205 (group shifted strings), 88 (21), 69/704/35 (34 and answer-space binary search), 206 (25), 70 (198), 496/503 (1944), 347/215 (top-k heap, quickselect), 540 (true/false-transition binary search), 125 (680), 904 (340 with k=2), 219/643/209 (sliding window, 346), 94 (173), 1480 (prefix sums), 207 (210), 312 (1547 interval DP).

## (c) MISSING, ranked by likelihood

Rank = composite position, plus any dated report. "30d 50" means 50% frequency in snehasishroy's 30-day list.

| # | LC | Name | Pattern | Frequency signal | Why it matters |
|---|---|---|---|---|---|
| 1 | 42 | Trapping Rain Water | two pointers / monostack | composite #4; 30d 75 | Top hard in every window; two-pointer proof is a classic follow-up |
| 2 | 560 | Subarray Sum Equals K | prefix sum + hashmap | #17; 30d 50; reported Dec 2025 | You have no prefix-sum-count card at all |
| 3 | 128 | Longest Consecutive Sequence | hashset / DSU | #13; 30d 62.5; 2026 "sighted" list | O(n) argument is what gets probed |
| 4 | 15 (+16, 18) | 3Sum / 3Sum Closest / 4Sum | sort + two pointers | #7, #28, #39 | Dedup logic is a common bug source; 167 only covers 2Sum |
| 5 | 5 | Longest Palindromic Substring | expand-around-centre / DP | #20; 3m 62.5 | No palindrome-DP card |
| 6 | 84 (+85) | Largest Rectangle in Histogram / Maximal Rectangle | monotonic stack | #47; 30d 50; 85: 6m 37.5 | Monostack depth is thin (only 1944) |
| 7 | 53 (+152, 918) | Maximum Subarray / Product / Circular | Kadane | #58; 6m 62.5 | Standard follow-up chain |
| 8 | 238 | Product of Array Except Self | prefix/suffix | #60; 6m 50 | "No division" follow-up |
| 9 | 54 (+48, 73) | Spiral Matrix / Rotate Image / Set Matrix Zeroes | matrix simulation | #29, #71; 30d 50 | Google loves index-careful simulation |
| 10 | 287 | Find the Duplicate Number | Floyd cycle / binary search on value | #44; 30d 50 | Constraint-twist follow-ups (O(1) space, read-only) |
| 11 | 41 | First Missing Positive | in-place index hashing | #63; 6m 37.5 | Pattern absent from inventory |
| 12 | 2 (+19, 148, 141) | Add Two Numbers / Remove Nth / Sort List / Cycle | linked list | #2, #98, #76, #96 | Only 2 linked-list cards |
| 13 | 50 (+69) | Pow(x, n) | fast exponentiation | #26; 30d 62.5 | Math gap; negative-exponent edge cases |
| 14 | 7 / 8 | Reverse Integer / String to Integer (atoi) | overflow-safe parsing | #11, #79; 30d 62.5 / 50 | Edge-case discipline is graded at L5 |
| 15 | 189 | Rotate Array | reversal trick | #18; 30d 62.5 | Cheap, frequent |
| 16 | 169 (+3737) | Majority Element / Count Subarrays With Majority Element I | Boyer–Moore / prefix balance | #12; 3737 30d 37.5 | 3737 is a 2025–26 newcomer on the list |
| 17 | 10 (+44) | Regex / Wildcard Matching | 2D string DP | #83; 44 all-time 50 | No 2D string-matching DP in the inventory beyond 72 |
| 18 | 1406 | Stone Game III | game / minimax DP | #87; 30d 37.5 | Game DP is underrepresented |
| 19 | 315 (+493) | Count of Smaller After Self / Reverse Pairs | merge-sort count / BIT | 315: 30d 37.5 + 2026 sighted; 493 #95 | No inversion-count card |
| 20 | 45 / 55 | Jump Game II / Jump Game | greedy reach | #74, #91; 6m 50 | Greedy-on-array gap |
| 21 | 31 | Next Permutation | array manipulation | 6m 50 | Frequently asked as a warm-up at Google |
| 22 | 912 | Sort an Array | implement merge/quick sort | #59; 30d 50 | Write a sort from scratch without bugs |
| 23 | 3699 | Number of ZigZag Arrays I | DP + prefix-sum optimisation | 30d 50 (newest entry) | Recent; tests DP-to-prefix-sum speedup |
| 24 | 974 | Subarray Sums Divisible by K | prefix mod + hashmap | 30d 37.5 | Pairs with 560 |
| 25 | 1838 | Frequency of the Most Frequent Element | sort + sliding window | 30d 37.5; 6m 37.5 | Window plus budget invariant |
| 26 | 2007 | Find Original Array From Doubled Array | greedy + counter | 30d 37.5 | Sorted-greedy matching |
| 27 | 907 | Sum of Subarray Minimums | monostack contribution | 6m 37.5 | Contribution technique |
| 28 | 32 | Longest Valid Parentheses | stack / DP | 6m 37.5 | Stack variant beyond matching |
| 29 | 815 | Bus Routes | BFS on routes | 3m/6m 25 | Graph modelling choice is the test |
| 30 | 68 | Text Justification | string simulation | 3m 25; all-time 50 | Classic Google; pure implementation |
| 31 | 297 | Serialize/Deserialize Binary Tree | tree DFS / design | 3m 25 | Class format; no tree-serialisation card |
| 32 | 981 (+1146, 2034) | Time-Based KV / Snapshot Array / Stock Price Fluctuation | versioned design + bisect | 3m/6m 25; 1146, 2034 6m 12.5 | Exactly the "design a class" format |
| 33 | 174 | Dungeon Game | reverse grid DP | 2026 sighted (snippet) | Backwards-DP insight |
| 34 | 2188 | Minimum Time to Finish the Race | DP + precompute | 2026 sighted; 6m 25 | Google-original-flavoured |
| 35 | 843 | Guess the Word | interactive / minimax | 6m 25; all-time 50 | Interactive API format |
| 36 | 23 | Merge k Sorted Lists | heap merge | all-time 50 | Streaming merge follow-ups |
| 37 | 1526 | Min Increments to Form Target Array | greedy difference | all-time 62.5 | One-line insight that Google likes |

Trivial easies that are MISSING but high on the lists (do them as a 30-minute warm-up batch, not as study items): 1, 9, 121/122, 14, 13, 26/27/80, 217, 268, 202, 283, 344, 1768, 485, 876, 231, 58, 605, 101.

## (d) Must-do shortlist (20)

| # | LC | Name | Pattern |
|---|---|---|---|
| 1 | 42 | Trapping Rain Water | two pointers / monostack |
| 2 | 560 (+974) | Subarray Sum Equals K | prefix sum + hashmap |
| 3 | 128 | Longest Consecutive Sequence | hashset |
| 4 | 84 (+85) | Largest Rectangle in Histogram | monotonic stack |
| 5 | 15 (+16) | 3Sum | sort + two pointers |
| 6 | 5 | Longest Palindromic Substring | expand / DP |
| 7 | 53 (+152) | Maximum Subarray | Kadane |
| 8 | 238 | Product of Array Except Self | prefix/suffix |
| 9 | 54 (+48) | Spiral Matrix | matrix simulation |
| 10 | 287 | Find the Duplicate Number | Floyd / value binary search |
| 11 | 41 | First Missing Positive | in-place index hashing |
| 12 | 10 | Regular Expression Matching | 2D DP |
| 13 | 1406 | Stone Game III | game DP |
| 14 | 315 (+493) | Count of Smaller Numbers After Self | merge sort / BIT |
| 15 | 2 (+19) | Add Two Numbers | linked list |
| 16 | 50 (+8) | Pow(x, n) / atoi | math / overflow |
| 17 | 45 (+55) | Jump Game II | greedy |
| 18 | 981 (+1146) | Time Based Key-Value Store | design class + bisect |
| 19 | 2812 | Find the Safest Path in a Grid | multi-source BFS + maximin path (weak VARIANT of 994 + 1102; reported Dec 2025 L5, 30d 37.5) |
| 20 | 68 | Text Justification | string simulation |

## (e) Pattern-level gaps (fewer than 3 problems in the inventory, but Google asks them often)

| Pattern | Inventory count | Google signal | Fill with |
|---|---|---|---|
| Prefix sum + hashmap counting | 0 (difference arrays only) | 560, 974, 525, 2D prefix sum (Dec 2025 L5) | 560, 974, 304 |
| Monotonic stack | 1 (1944) plus 239 deque | 84, 85, 42, 496/503, 739, 907 | 84, 907, 739 |
| Kadane / 1D max-subarray | 0 | 53, 152, 918, 121 | 53, 152 |
| 2D string DP (regex, palindrome, LCS) | 1 (72) plus 727 | 5, 10, 44, 1143 | 10, 5 |
| Game / minimax DP | 1 (913) | 1406, 877, 843 | 1406 |
| Inversion counting (merge sort, BIT) | 0 (2407 segment tree only) | 315, 493 | 315 |
| Math / overflow / bit | ~0 | 7, 8, 9, 50, 69, 231, 191 | 50, 8, 7 |
| Linked list | 2 (21, 25) | 2, 19, 141, 148, 23, 206 | 2, 148, 23 |
| Matrix simulation | 1 (crossword) plus zigzag | 54, 48, 73, 68 | 54, 48, 68 |
| Array greedy (reachability) | 0 (interval greedy is fine) | 55, 45, 1526, 134 | 45, 1526 |
| In-place index tricks / cyclic sort | 0 | 41, 287, 268, 448 | 41, 287 |
| Versioned / timestamped design + bisect | 0 (strong on other design) | 981, 1146, 2034 | 981, 1146 |
| k-Sum (sort + two pointers) | 1 (167) | 15, 16, 18 | 15 |

**Not gaps:** binary search (more than 8 items), sliding window, intervals and sweep line, graph BFS/Dijkstra/topological sort/DSU, tries, parsing and recursion, iterator/LRU/LFU design.

## (f) Google-specific style notes

- **Original problems, classic cores.** Recent reports describe disguised problems: rental-car fleet assignment (≈ meeting rooms / min-heap), safest path with zombies (2812), RPC or event timeout detection (sliding window or heap over logs), playlist shuffle without repeating the last K (hashset plus array swap, O(1) per pick), and template substitution with cycle detection (you have 3481). Practise saying out loud "this is X in disguise" within the first 5 minutes.
- **Follow-up ladder.** L5 rounds typically go from a brute-force solution, to the optimal one, then to a changed constraint. Examples: 200 becomes "grid updated online", which is 305 with DSU. 410 is DP first, then binary search on the answer. Union-find gets probed on path compression and rank. Prepare one follow-up per shortlist item (e.g. 42 into 2D 407; 560 into "count of positive-only" via a sliding window; 128 as a stream with DSU).
- **Scaling the input.** Expect "the data doesn't fit in memory or arrives across shards" (e.g. "Process Sharded Login Logs"). Have ready answers for external sort / k-way merge (23), counting sketches, and per-shard top-k followed by a merge.
- **Streaming.** Moving average, median, hit counter and rate limiter are already in the inventory. Add a sliding-window max over a stream and "top-k in the last T seconds" (heap with lazy deletion).
- **Design-a-class format.** You may be handed a class with several methods where the algorithm sits in one of them, and interface cleanliness is graded. Rehearse 981, 1146 and 2034 with clean method boundaries, type hints, and complexity per method.
- **Environment.** No code execution (Docs or a basic editor). Dry-run on a small example by hand and call out edge cases (empty input, overflow, duplicates) before the interviewer does. At L5, writing bug-free code on the first pass and driving the edge-case discussion yourself both count.
