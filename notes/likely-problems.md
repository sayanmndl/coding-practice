Yes. I treated this as a **Google L5/Senior SWE coding optimization problem**, not a generic LeetCode list.

The strongest recent signal is that Google still uses medium-to-hard DSA, but often wraps the underlying algorithm in an unfamiliar story and then changes constraints. Recent L5 reports feature interval/sweep problems, graphs/topological sorting, grids, randomized/streaming structures, DP, and data-structure/API questions; recent Google interviewer commentary emphasizes explaining the model, writing clean correct code, testing, and reacting to follow-ups. ([LeetCode][1])

I used roughly this ranking model: **Google-specific/recent evidence ~35%, pattern transferability ~20%, source diversity ~10%, L5/senior follow-up value ~15%, difficulty/interview fit ~10%, and ML/infra/streaming relevance ~10%**. I applied a small penalty to problems you've already practiced heavily, but not enough to bury genuinely important Google patterns. The ranking is a **reasoned probability/value ranking**, not a claim that Google publishes question frequencies.

Recent company-tag datasets are useful as one aggregated signal, but they're noisy and incomplete, so I did not simply sort them by frequency. ([GitHub][2])

---

# Tier S — #1–50: Must master

| Rank | Problem                                                                                       | Difficulty | Primary Pattern              | Google Relevance | Why it is here                                                                                                                          |
| ---- | --------------------------------------------------------------------------------------------- | ---------- | ---------------------------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| #1   | **LC 269: Alien Dictionary**                                                                  | Hard       | Graph / topological sort     | Very High        | Canonical Google-style DAG inference; ordering/topological variants continue to appear in recent reports. ([LeetCode][3])               |
| #2   | **LC 2402: Meeting Rooms III**                                                                | Hard       | Intervals / heaps            | Very High        | A recent L5 SWE/ML report described a tricky Meeting Rooms III variant; superb simulation + heap training. ([LeetCode][4])              |
| #3   | **LC 715: Range Module**                                                                      | Hard       | Intervals / ordered map      | Very High        | Explicitly reported in a January 2025 L5 loop, with point query followed by range-query generalization. ([LeetCode][1])                 |
| #4   | **LC 2392: Build a Matrix With Conditions**                                                   | Hard       | Topological sort / DAG       | Very High        | Explicitly named in a recent L5 coding experience; combines two dependency graphs plus construction. ([LeetCode][5])                    |
| #5   | **LC 380: Insert Delete GetRandom O(1)**                                                      | Medium     | DS design / randomization    | Very High        | Bay Area L5 report had a close variant plus complexity optimization; excellent API/data-structure problem. ([LeetCode][6])              |
| #6   | **Reported variant: Worker Shift Timeline / Active Workers by Interval** — closest: LC 56/253 | Medium     | Sweep line / intervals       | Very High        | Direct January 2025 L5 question: transform worker shifts into maximal intervals with active-worker sets. ([LeetCode][1])                |
| #7   | **LC 399: Evaluate Division**                                                                 | Medium     | Graph DFS/BFS                | Very High        | Excellent implicit-graph modeling; representative of Google's tendency to hide standard graph structure behind a story.                 |
| #8   | **LC 1101: The Earliest Moment When Everyone Become Friends**                                 | Medium     | Union-Find                   | Very High        | Bay Area L5 round used a complex variant and then pushed toward a distributed version. ([LeetCode][6])                                  |
| #9   | **LC 636: Exclusive Time of Functions**                                                       | Medium     | Stack / simulation           | Very High        | A simplified version appeared in a Bay Area L5 onsite; tests precise event semantics and invariants. ([LeetCode][6])                    |
| #10  | **LC 210: Course Schedule II**                                                                | Medium     | Topological sort             | Very High        | Dependency/order graph is one of the most transferable Google patterns. You've seen it, so practice variants rather than memorizing it. |
| #11  | **LC 127: Word Ladder**                                                                       | Hard       | BFS / implicit graph         | Very High        | Classic graph-modeling question; especially valuable for bidirectional-BFS and memory follow-ups.                                       |
| #12  | **LC 732: My Calendar III**                                                                   | Hard       | Sweep line / segment tree    | Very High        | Dynamic intervals, updates and range aggregation give an interviewer multiple follow-up directions.                                     |
| #13  | **LC 295: Find Median from Data Stream**                                                      | Hard       | Heaps / streaming            | Very High        | Particularly relevant for an ML/infra engineer: online state, bounded memory, heaps and scalability.                                    |
| #14  | **LC 394: Decode String**                                                                     | Medium     | Stack / recursion            | Very High        | Strong parsing problem where correctness and state handling matter more than obscure tricks.                                            |
| #15  | **LC 743: Network Delay Time**                                                                | Medium     | Dijkstra / graph             | Very High        | Mandatory shortest-path fluency and clean complexity discussion.                                                                        |
| #16  | **LC 787: Cheapest Flights Within K Stops**                                                   | Medium     | Shortest path / DP           | Very High        | Forces you to model state correctly and distinguish BFS/DP/Bellman-Ford/Dijkstra variants.                                              |
| #17  | **LC 300: Longest Increasing Subsequence**                                                    | Medium     | DP / binary search           | Very High        | Ideal Google progression: obvious DP → O(n log n) optimization and proof.                                                               |
| #18  | **LC 505: The Maze II**                                                                       | Medium     | Dijkstra / grid              | Very High        | A weighted shortest-path problem disguised as matrix traversal.                                                                         |
| #19  | **LC 721: Accounts Merge**                                                                    | Medium     | Union-Find / graph           | Very High        | Practical identity/connectivity modeling plus alternate DFS/DSU implementations.                                                        |
| #20  | **Reported variant: Visited Files/Directories Compression** — closest: LC 588/1166            | Medium     | Tree / trie / postorder      | Very High        | Recent L5 question: return visited files, but collapse a fully visited subtree into the directory itself. ([LeetCode][7])               |
| #21  | **LC 1851: Minimum Interval to Include Each Query**                                           | Hard       | Sweep line / heap            | Very High        | Offline-query transformation combines sorting, interval reasoning and heaps.                                                            |
| #22  | **LC 200: Number of Islands**                                                                 | Medium     | Grid DFS/BFS                 | Very High        | You already know it; retain as the baseline for harder connectivity/grid mutations.                                                     |
| #23  | **LC 218: The Skyline Problem**                                                               | Hard       | Sweep line / heap            | Very High        | Excellent event ordering, lazy heap deletion and boundary-condition exercise.                                                           |
| #24  | **LC 547: Number of Provinces**                                                               | Medium     | Graph / Union-Find           | Very High        | Quick connectivity baseline: know DFS, BFS and DSU versions cold.                                                                       |
| #25  | **LC 329: Longest Increasing Path in a Matrix**                                               | Hard       | DFS + memo / DAG             | Very High        | Hidden DAG + memoization is quintessential high-value Google pattern recognition.                                                       |
| #26  | **Reported variant: Root a Degree-3 Tree Under Layer-Color Constraints**                      | Hard       | Tree / graph / rerooting     | High             | Recent L5 question with increasingly difficult color-cycle constraints after selecting a valid root. ([LeetCode][1])                    |
| #27  | **LC 253: Meeting Rooms II**                                                                  | Medium     | Intervals / heap             | High             | Baseline scheduling primitive behind several harder Google variants.                                                                    |
| #28  | **LC 417: Pacific Atlantic Water Flow**                                                       | Medium     | Reverse DFS/BFS              | High             | Rewards reversing the problem rather than brute-forcing from every cell.                                                                |
| #29  | **LC 490: The Maze**                                                                          | Medium     | Grid graph                   | High             | Strong state-transition modeling and useful precursor to Maze II.                                                                       |
| #30  | **LC 207: Course Schedule**                                                                   | Medium     | Graph cycle detection        | High             | Know DFS colors and Kahn's algorithm, and explain their tradeoffs.                                                                      |
| #31  | **LC 759: Employee Free Time**                                                                | Hard       | Intervals / heap             | High             | Multi-list scheduling with natural streaming/generalization follow-ups.                                                                 |
| #32  | **LC 435: Non-overlapping Intervals**                                                         | Medium     | Greedy / intervals           | High             | Important greedy proof and interval-choice invariant.                                                                                   |
| #33  | **LC 752: Open the Lock**                                                                     | Medium     | BFS / state graph            | High             | Trains converting states and legal transitions into an implicit graph.                                                                  |
| #34  | **Reported variant: Hierarchical Path/Domain Value Aggregation**                              | Medium     | Trie / tree aggregation      | High             | A recent Google interview involved hierarchical path/domain values contributing to ancestors. ([LeetCode][8])                           |
| #35  | **LC 452: Minimum Number of Arrows to Burst Balloons**                                        | Medium     | Greedy / intervals           | High             | Clean interval-greedy reasoning and proof.                                                                                              |
| #36  | **LC 731: My Calendar II**                                                                    | Medium     | Sweep line / intervals       | High             | Excellent bridge from basic interval overlap to dynamic event structures.                                                               |
| #37  | **LC 1584: Min Cost to Connect All Points**                                                   | Medium     | MST                          | High             | Gives Prim/Kruskal/DSU choices and useful complexity tradeoffs.                                                                         |
| #38  | **LC 684: Redundant Connection**                                                              | Medium     | Union-Find                   | High             | Basic DSU should be automatic before harder dynamic connectivity.                                                                       |
| #39  | **LC 444: Sequence Reconstruction**                                                           | Medium     | Topological sort             | High             | Tests whether an ordering is not merely valid but unique.                                                                               |
| #40  | **Reported variant: Router Broadcast Reachability in 2D**                                     | Medium     | Graph construction + BFS/DFS | High             | Reported again in 2026: derive edges from geometric range, then determine reachability. ([LeetCode][9])                                 |
| #41  | **LC 133: Clone Graph**                                                                       | Medium     | Graph traversal              | High             | Visited-state/reference handling and graph-copy invariants.                                                                             |
| #42  | **LC 1094: Car Pooling**                                                                      | Medium     | Sweep line / prefix sum      | High             | Simple problem, but extremely useful for event-delta thinking.                                                                          |
| #43  | **LC 332: Reconstruct Itinerary**                                                             | Hard       | Eulerian path                | High             | Good example of a less-obvious graph algorithm that remains interview-feasible.                                                         |
| #44  | **LC 56: Merge Intervals**                                                                    | Medium     | Intervals                    | High             | Foundational; solve nearly instantly and focus on explanation/edge cases.                                                               |
| #45  | **LC 57: Insert Interval**                                                                    | Medium     | Intervals                    | High             | Tests maintaining invariants while handling boundaries.                                                                                 |
| #46  | **LC 729: My Calendar I**                                                                     | Medium     | Ordered intervals            | High             | Natural API/design framing around overlap checking.                                                                                     |
| #47  | **LC 286: Walls and Gates**                                                                   | Medium     | Multi-source BFS             | High             | Multi-source BFS must be instinctive.                                                                                                   |
| #48  | **Reported variant: Most-Active Chat Speaker + streaming follow-ups**                         | Medium     | Heap / streaming / hash      | High             | An L5 candidate reported this seemingly simple question becoming difficult through follow-ups. ([LeetCode][7])                          |
| #49  | **LC 994: Rotting Oranges**                                                                   | Medium     | Multi-source BFS             | High             | Another clean multi-source propagation representative.                                                                                  |
| #50  | **LC 480: Sliding Window Median**                                                             | Hard       | Heaps / sliding window       | High             | Combines online state, deletion, balancing and careful invariants.                                                                      |

---

# Tier A — #51–100: Very high priority

| Rank | Problem                                                                      | Difficulty | Primary Pattern          | Google Relevance | Why it is here                                                                                                                    |
| ---- | ---------------------------------------------------------------------------- | ---------- | ------------------------ | ---------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| #51  | **LC 642: Design Search Autocomplete System**                                | Hard       | Trie / heap              | High             | Trie plus ranking plus design/API discussion.                                                                                     |
| #52  | **LC 212: Word Search II**                                                   | Hard       | Trie / backtracking      | High             | Excellent combination of pruning and grid search.                                                                                 |
| #53  | **LC 560: Subarray Sum Equals K**                                            | Medium     | Prefix sum / hash        | High             | Must know the prefix-frequency transformation immediately.                                                                        |
| #54  | **Reported variant: Longest Consecutive-Neighbor Path in Grid**              | Medium     | Grid BFS/DFS / memo      | High             | Recent L5 coding problem; closely exercises grid-state traversal and optimization. ([LeetCode][7])                                |
| #55  | **LC 692: Top K Frequent Words**                                             | Medium     | Heap / trie              | High             | Top-k ordering, tie-breakers and comparator correctness.                                                                          |
| #56  | **LC 703: Kth Largest Element in a Stream**                                  | Easy       | Heap / streaming         | High             | Simple but highly relevant online-data primitive.                                                                                 |
| #57  | **LC 525: Contiguous Array**                                                 | Medium     | Prefix sum / hash        | High             | Excellent "state seen before" prefix transformation.                                                                              |
| #58  | **LC 523: Continuous Subarray Sum**                                          | Medium     | Prefix sum / modular     | High             | Modular-prefix invariant and subtle edge cases.                                                                                   |
| #59  | **LC 588: Design In-Memory File System**                                     | Hard       | Trie / design            | High             | Especially strong for L5: API design + hierarchical structures.                                                                   |
| #60  | **LC 974: Subarray Sums Divisible by K**                                     | Medium     | Prefix sum / modular     | High             | Generalizes prefix-frequency reasoning.                                                                                           |
| #61  | **LC 930: Binary Subarrays With Sum**                                        | Medium     | Prefix / sliding window  | High             | Useful to compare prefix-count and at-most-window approaches.                                                                     |
| #62  | **LC 238: Product of Array Except Self**                                     | Medium     | Prefix/suffix            | High             | Good space-optimization follow-up.                                                                                                |
| #63  | **Reported variant: Stream Processor — successive time/space optimizations** | Medium     | Streaming / DS           | High             | A successful L5 report explicitly described naive → time optimized → space optimized → both optimized. ([LeetCode][10])           |
| #64  | **LC 378: Kth Smallest Element in Sorted Matrix**                            | Medium     | Heap / binary search     | High             | Two substantially different optimal approaches and good tradeoff discussion.                                                      |
| #65  | **LC 42: Trapping Rain Water**                                               | Hard       | Two pointers / stack     | High             | Multiple solutions; ideal for invariant explanation.                                                                              |
| #66  | **LC 239: Sliding Window Maximum**                                           | Hard       | Monotonic deque          | High             | Essential deque invariant.                                                                                                        |
| #67  | **LC 528: Random Pick with Weight**                                          | Medium     | Prefix sum / randomness  | High             | Randomization questions recur in senior reports.                                                                                  |
| #68  | **LC 1166: Design File System**                                              | Medium     | Trie / design            | High             | Hierarchical APIs and path parsing.                                                                                               |
| #69  | **LC 76: Minimum Window Substring**                                          | Hard       | Sliding window           | High             | Know the window invariant without memorizing implementation.                                                                      |
| #70  | **LC 621: Task Scheduler**                                                   | Medium     | Greedy / heap            | High             | Scheduling plus alternative closed-form reasoning.                                                                                |
| #71  | **LC 3: Longest Substring Without Repeating Characters**                     | Medium     | Sliding window           | High             | Baseline sliding-window fluency.                                                                                                  |
| #72  | **Reported variant: Logger/Timer with incremental constraints**              | Medium     | Hash / queue / streaming | High             | A Google MLE L6 report specifically described a logger/timer problem whose constraints were repeatedly extended. ([LeetCode][11]) |
| #73  | **LC 23: Merge k Sorted Lists**                                              | Hard       | Heap                     | High             | K-way merging and streaming generalization.                                                                                       |
| #74  | **LC 767: Reorganize String**                                                | Medium     | Heap / greedy            | High             | Priority-queue scheduling under constraints.                                                                                      |
| #75  | **LC 424: Longest Repeating Character Replacement**                          | Medium     | Sliding window           | High             | Strong window-invariant exercise.                                                                                                 |
| #76  | **LC 31: Next Permutation**                                                  | Medium     | Array / greedy           | Med-High         | Tests derivation rather than a standard container.                                                                                |
| #77  | **LC 358: Rearrange String k Distance Apart**                                | Hard       | Heap / greedy            | Med-High         | More difficult scheduling variant.                                                                                                |
| #78  | **LC 438: Find All Anagrams in a String**                                    | Medium     | Sliding window           | Med-High         | Fixed-length frequency-window fluency.                                                                                            |
| #79  | **LC 30: Substring with Concatenation of All Words**                         | Hard       | Sliding window / hash    | Med-High         | Nontrivial window alignment and state management.                                                                                 |
| #80  | **Reported variant: Generate Strings from a Simplified Regex Pattern**       | Medium     | Backtracking / parsing   | Med-High         | Bay Area L5 phone screen reported this exact style of backtracking question. ([LeetCode][6])                                      |
| #81  | **LC 347: Top K Frequent Elements**                                          | Medium     | Heap / bucket            | Med-High         | Know heap, bucket and quickselect possibilities.                                                                                  |
| #82  | **LC 472: Concatenated Words**                                               | Hard       | Trie / DP                | Med-High         | Strong trie/DP decomposition.                                                                                                     |
| #83  | **LC 215: Kth Largest Element in an Array**                                  | Medium     | Quickselect / heap       | Med-High         | Quickselect deserves special attention for Google.                                                                                |
| #84  | **LC 373: Find K Pairs with Smallest Sums**                                  | Medium     | Heap                     | Med-High         | Best-first exploration with a bounded frontier.                                                                                   |
| #85  | **LC 11: Container With Most Water**                                         | Medium     | Two pointers             | Med-High         | Simple but tests whether you can justify eliminating search space.                                                                |
| #86  | **LC 15: 3Sum**                                                              | Medium     | Two pointers / sorting   | Med-High         | Foundational sorted two-pointer reasoning.                                                                                        |
| #87  | **LC 895: Maximum Frequency Stack**                                          | Hard       | DS design                | Med-High         | Excellent hash + grouped state design.                                                                                            |
| #88  | **LC 18: 4Sum**                                                              | Medium     | Sorting / two pointers   | Med-High         | Generalization and duplicate handling.                                                                                            |
| #89  | **LC 460: LFU Cache**                                                        | Hard       | DS design                | Med-High         | L5-worthy invariant and API/data-structure construction.                                                                          |
| #90  | **LC 41: First Missing Positive**                                            | Hard       | In-place hashing         | Med-High         | Unusual but transferable O(1)-space array transformation.                                                                         |
| #91  | **LC 470: Implement Rand10() Using Rand7()**                                 | Medium     | Rejection sampling       | Med-High         | Randomization/probability is disproportionately useful for Google.                                                                |
| #92  | **LC 128: Longest Consecutive Sequence**                                     | Medium     | Hash set                 | Med-High         | Linear-time set invariant.                                                                                                        |
| #93  | **LC 49: Group Anagrams**                                                    | Medium     | Hashing                  | Med-High         | Basic canonicalization pattern.                                                                                                   |
| #94  | **LC 973: K Closest Points to Origin**                                       | Medium     | Heap / quickselect       | Med-High         | You've seen it; revisit mainly for quickselect and streaming versions.                                                            |
| #95  | **LC 355: Design Twitter**                                                   | Medium     | Design / heap            | Med-High         | Merge feeds + APIs + complexity discussion.                                                                                       |
| #96  | **LC 981: Time Based Key-Value Store**                                       | Medium     | Binary search / design   | Med-High         | Practical storage API and append-only histories.                                                                                  |
| #97  | **LC 1146: Snapshot Array**                                                  | Medium     | Binary search / design   | Med-High         | Persistent/versioned state is relevant to infra work.                                                                             |
| #98  | **LC 173: BST Iterator**                                                     | Medium     | Iterator / tree          | Med-High         | Laziness and amortized complexity.                                                                                                |
| #99  | **LC 208: Implement Trie**                                                   | Medium     | Trie                     | Med-High         | Trie fundamentals must be automatic.                                                                                              |
| #100 | **LC 211: Design Add and Search Words**                                      | Medium     | Trie / DFS               | Med-High         | Trie plus wildcard search.                                                                                                        |

---

# Tier B — #101–175: Strong coverage

| Rank | Problem                                            | Difficulty | Primary Pattern         | Google Relevance | Why it is here                                                                                                            |
| ---- | -------------------------------------------------- | ---------- | ----------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------- |
| #101 | LC 336: Palindrome Pairs                           | Hard       | Trie / hashing          | Med-High         | Strong nontrivial string-indexing exercise.                                                                               |
| #102 | LC 146: LRU Cache                                  | Medium     | DS design               | Med-High         | You've practiced it; retain for design fluency.                                                                           |
| #103 | LC 398: Random Pick Index                          | Medium     | Reservoir sampling      | Med-High         | Essential streaming sampling primitive.                                                                                   |
| #104 | LC 432: All O(1) Data Structure                    | Hard       | DS design               | Med-High         | You've seen it; useful mainly for invariant mastery.                                                                      |
| #105 | LC 648: Replace Words                              | Medium     | Trie                    | Med-High         | Lightweight trie application.                                                                                             |
| #106 | LC 382: Linked List Random Node                    | Medium     | Reservoir sampling      | Med-High         | Reservoir sampling from unknown-length input.                                                                             |
| #107 | LC 745: Prefix and Suffix Search                   | Hard       | Trie                    | Med-High         | Compound indexing and memory tradeoffs.                                                                                   |
| #108 | LC 497: Random Point in Non-overlapping Rectangles | Medium     | Prefix sum / randomness | Med-High         | Weighted sampling plus geometry.                                                                                          |
| #109 | LC 388: Longest Absolute File Path                 | Medium     | Stack / parsing         | Med-High         | Hierarchical text parsing with precise state.                                                                             |
| #110 | LC 1: Two Sum                                      | Easy       | Hash map                | Med-High         | Not because Google will ask vanilla Two Sum—because the lookup transformation should be instantaneous.                    |
| #111 | LC 341: Flatten Nested List Iterator               | Medium     | Iterator / stack        | Med-High         | Already seen; revisit lazy vs eager designs.                                                                              |
| #112 | LC 384: Shuffle an Array                           | Medium     | Randomization           | Med-High         | Fisher–Yates and proof of uniformity.                                                                                     |
| #113 | LC 284: Peeking Iterator                           | Medium     | Iterator design         | Med-High         | Small API/state problem.                                                                                                  |
| #114 | LC 251: Flatten 2D Vector                          | Medium     | Iterator design         | Med-High         | Iterator state and empty-range handling.                                                                                  |
| #115 | LC 124: Binary Tree Maximum Path Sum               | Hard       | Tree DP                 | Med-High         | Core postorder-state formulation.                                                                                         |
| #116 | LC 900: RLE Iterator                               | Medium     | Iterator / simulation   | Med-High         | Amortized processing of compressed streams.                                                                               |
| #117 | LC 710: Random Pick with Blacklist                 | Hard       | Randomization / hashing | Med-High         | Clever remapping with strong proof component.                                                                             |
| #118 | LC 519: Random Flip Matrix                         | Medium     | Randomization / hashing | Med-High         | Sampling without replacement at scale.                                                                                    |
| #119 | LC 410: Split Array Largest Sum                    | Hard       | Binary search on answer | Med-High         | Excellent feasibility predicate + monotonicity problem.                                                                   |
| #120 | LC 297: Serialize and Deserialize Binary Tree      | Hard       | Tree / design           | Med-High         | API contract, serialization and iterative follow-ups.                                                                     |
| #121 | LC 74: Search a 2D Matrix                          | Medium     | Binary search           | Med-High         | Binary-search invariant baseline.                                                                                         |
| #122 | LC 609: Find Duplicate File in System              | Medium     | Hash / parsing          | Med-High         | Practical file-system flavored hashing.                                                                                   |
| #123 | LC 33: Search in Rotated Sorted Array              | Medium     | Binary search           | Med-High         | Must be fluent in nontrivial binary-search invariants.                                                                    |
| #124 | LC 968: Binary Tree Cameras                        | Hard       | Tree greedy / DP        | Med-High         | Excellent local-state tree reasoning.                                                                                     |
| #125 | LC 34: First/Last Position in Sorted Array         | Medium     | Binary search           | Med-High         | Lower/upper-bound primitives.                                                                                             |
| #126 | LC 153: Find Minimum in Rotated Sorted Array       | Medium     | Binary search           | Med-High         | Clean rotated-array invariant.                                                                                            |
| #127 | LC 162: Find Peak Element                          | Medium     | Binary search           | Med-High         | Binary search over directional information.                                                                               |
| #128 | LC 875: Koko Eating Bananas                        | Medium     | Binary search on answer | Med-High         | Canonical monotonic feasibility.                                                                                          |
| #129 | LC 1011: Capacity To Ship Packages Within D Days   | Medium     | Binary search on answer | Med-High         | Excellent feasibility-function practice.                                                                                  |
| #130 | LC 863: All Nodes Distance K in Binary Tree        | Medium     | Tree → graph BFS        | Med-High         | Converts tree into graph with parent links.                                                                               |
| #131 | LC 774: Minimize Max Distance to Gas Station       | Hard       | Binary search on answer | Med-High         | Numeric binary search and precision.                                                                                      |
| #132 | LC 4: Median of Two Sorted Arrays                  | Hard       | Binary search           | Med-High         | Hard but educational partition invariant.                                                                                 |
| #133 | LC 98: Validate BST                                | Medium     | Tree DFS                | Med-High         | Bounds/inorder alternatives.                                                                                              |
| #134 | LC 540: Single Element in Sorted Array             | Medium     | Binary search           | Med-High         | Parity-based invariant.                                                                                                   |
| #135 | LC 236: LCA of Binary Tree                         | Medium     | Tree DFS                | Med-High         | Fundamental recursive tree state.                                                                                         |
| #136 | LC 113: Path Sum II                                | Medium     | Tree / backtracking     | Med-High         | Path-state handling.                                                                                                      |
| #137 | LC 333: Largest BST Subtree                        | Medium     | Tree DP                 | Med-High         | Return multiple pieces of subtree state.                                                                                  |
| #138 | LC 240: Search a 2D Matrix II                      | Medium     | Matrix / two pointers   | Med-High         | Monotonic matrix elimination.                                                                                             |
| #139 | LC 437: Path Sum III                               | Medium     | Tree / prefix sum       | Med-High         | Prefix-sum technique transferred onto trees.                                                                              |
| #140 | LC 310: Minimum Height Trees                       | Medium     | Tree centers            | Med-High         | Leaf peeling and graph structure.                                                                                         |
| #141 | LC 834: Sum of Distances in Tree                   | Hard       | Rerooting DP            | Med-High         | One of the best reroot-DP representatives.                                                                                |
| #142 | LC 1245: Tree Diameter                             | Medium     | Tree / graph            | Med-High         | Two-pass traversal and tree metrics.                                                                                      |
| #143 | LC 102: Binary Tree Level Order Traversal          | Medium     | Tree BFS                | Med-High         | BFS baseline.                                                                                                             |
| #144 | LC 103: Zigzag Level Order                         | Medium     | Tree BFS                | Med-High         | Level-state variation.                                                                                                    |
| #145 | LC 69: Sqrt(x)                                     | Easy       | Binary search           | Med-High         | Boundary discipline.                                                                                                      |
| #146 | LC 199: Binary Tree Right Side View                | Medium     | BFS/DFS                 | Med-High         | Alternate BFS/DFS formulations.                                                                                           |
| #147 | LC 314: Binary Tree Vertical Order Traversal       | Medium     | Tree BFS                | Med-High         | Coordinate assignment plus ordering.                                                                                      |
| #148 | LC 987: Vertical Order Traversal                   | Hard       | Tree / sorting          | Med-High         | More demanding ordering/tie semantics.                                                                                    |
| #149 | LC 105: Build Tree from Preorder + Inorder         | Medium     | Recursion               | Med-High         | Recursive decomposition and indexing.                                                                                     |
| #150 | LC 106: Build Tree from Inorder + Postorder        | Medium     | Recursion               | Med-High         | Same transferable reconstruction pattern.                                                                                 |
| #151 | LC 889: Build Tree from Preorder + Postorder       | Medium     | Recursion               | Medium           | Ambiguity and recursive partitioning.                                                                                     |
| #152 | LC 235: LCA of BST                                 | Medium     | BST                     | Medium           | Exploit ordering rather than generic DFS.                                                                                 |
| #153 | LC 366: Find Leaves of Binary Tree                 | Medium     | Tree DFS                | Medium           | Height-as-removal-round insight.                                                                                          |
| #154 | LC 652: Find Duplicate Subtrees                    | Medium     | Tree hashing            | Medium           | Canonical subtree serialization/hash pattern.                                                                             |
| #155 | LC 543: Diameter of Binary Tree                    | Easy       | Tree DFS                | Medium           | You've seen N-ary diameter; keep generic tree-DP reflex.                                                                  |
| #156 | LC 742: Closest Leaf in Binary Tree                | Medium     | Tree + BFS              | Medium           | Tree-to-undirected-graph conversion.                                                                                      |
| #157 | LC 104: Maximum Depth of Binary Tree               | Easy       | Tree DFS/BFS            | Medium           | Basic recursion should be frictionless.                                                                                   |
| #158 | LC 250: Count Univalue Subtrees                    | Medium     | Tree DFS                | Medium           | Postorder boolean/state aggregation.                                                                                      |
| #159 | LC 79: Word Search                                 | Medium     | Backtracking            | Medium           | Grid-search baseline before Word Search II.                                                                               |
| #160 | LC 403: Frog Jump                                  | Hard       | DP / memoization        | Medium           | A recent Google interview report described a related DP story problem; strong state-definition practice. ([LeetCode][12]) |
| #161 | LC 44: Wildcard Matching                           | Hard       | DP / greedy             | Medium           | Difficult string-state DP.                                                                                                |
| #162 | LC 449: Serialize and Deserialize BST              | Medium     | BST / serialization     | Medium           | Exploit BST constraints for compact representation.                                                                       |
| #163 | LC 429: N-ary Tree Level Order                     | Medium     | BFS                     | Medium           | Useful non-binary-tree baseline.                                                                                          |
| #164 | LC 112: Path Sum                                   | Easy       | DFS                     | Medium           | Simple recursion under time pressure.                                                                                     |
| #165 | LC 131: Palindrome Partitioning                    | Medium     | Backtracking / DP       | Medium           | Precompute + enumerate.                                                                                                   |
| #166 | LC 10: Regular Expression Matching                 | Hard       | DP                      | Medium           | High educational value for state definition.                                                                              |
| #167 | LC 174: Dungeon Game                               | Hard       | Grid DP                 | Medium           | Reverse DP and non-obvious state semantics.                                                                               |
| #168 | LC 1522: Diameter of N-Ary Tree                    | Medium     | Tree DFS                | Medium           | You already studied it; retain, don't over-practice.                                                                      |
| #169 | LC 109: Sorted List to BST                         | Medium     | Tree / linked list      | Medium           | Recursive construction tradeoffs.                                                                                         |
| #170 | LC 52: N-Queens II                                 | Hard       | Backtracking / bitmask  | Medium           | Bitmask optimization on familiar backtracking.                                                                            |
| #171 | LC 37: Sudoku Solver                               | Hard       | Backtracking            | Medium           | Constraint search and pruning.                                                                                            |
| #172 | LC 425: Word Squares                               | Hard       | Trie / backtracking     | Medium           | Strong combined prefix-search/backtracking exercise.                                                                      |
| #173 | LC 46: Permutations                                | Medium     | Backtracking            | Medium           | Backtracking primitive.                                                                                                   |
| #174 | LC 47: Permutations II                             | Medium     | Backtracking            | Medium           | Duplicate-state handling.                                                                                                 |
| #175 | LC 426: BST to Sorted Doubly Linked List           | Medium     | BST / pointers          | Medium           | Tree traversal plus pointer mutation.                                                                                     |

---

# Tier C — #176–250: Broaden coverage

| Rank | Problem                                    | Difficulty | Primary Pattern        | Google Relevance | Why it is here                                                                                                         |
| ---- | ------------------------------------------ | ---------- | ---------------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------- |
| #176 | LC 77: Combinations                        | Medium     | Backtracking           | Medium           | Basic decision-tree enumeration.                                                                                       |
| #177 | LC 139: Word Break                         | Medium     | DP / trie              | Medium           | Segmentation DP baseline.                                                                                              |
| #178 | LC 230: Kth Smallest in BST                | Medium     | BST / inorder          | Medium           | Exploit traversal ordering.                                                                                            |
| #179 | LC 39: Combination Sum                     | Medium     | Backtracking           | Medium           | Search-space pruning.                                                                                                  |
| #180 | LC 285: Inorder Successor in BST           | Medium     | BST                    | Medium           | Parentless successor reasoning.                                                                                        |
| #181 | LC 40: Combination Sum II                  | Medium     | Backtracking           | Medium           | Deduplication under recursion.                                                                                         |
| #182 | LC 140: Word Break II                      | Hard       | DP / backtracking      | Medium           | Memoization + output-sensitive enumeration.                                                                            |
| #183 | LC 450: Delete Node in BST                 | Medium     | BST                    | Medium           | Pointer/case reasoning.                                                                                                |
| #184 | LC 78: Subsets                             | Medium     | Backtracking / bitmask | Medium           | Enumeration primitive.                                                                                                 |
| #185 | LC 701: Insert into BST                    | Medium     | BST                    | Medium           | BST basics.                                                                                                            |
| #186 | LC 90: Subsets II                          | Medium     | Backtracking           | Medium           | Duplicate control.                                                                                                     |
| #187 | LC 99: Recover BST                         | Medium     | BST / inorder          | Medium           | Inorder anomaly reasoning.                                                                                             |
| #188 | LC 22: Generate Parentheses                | Medium     | Backtracking           | Medium           | Constraint-preserving generation.                                                                                      |
| #189 | LC 308: Range Sum Query 2D — Mutable       | Hard       | Fenwick / segment tree | Medium           | Important because Google has historically used 2D query/update questions with scalability follow-ups. ([LeetCode][13]) |
| #190 | LC 51: N-Queens                            | Hard       | Backtracking           | Medium           | You've seen it; maintain pattern only.                                                                                 |
| #191 | LC 1382: Balance a BST                     | Medium     | BST                    | Medium           | Rebuild vs rotations discussion.                                                                                       |
| #192 | LC 301: Remove Invalid Parentheses         | Hard       | BFS / backtracking     | Medium           | Minimum-edit search and pruning.                                                                                       |
| #193 | LC 72: Edit Distance                       | Medium     | DP                     | Medium           | Foundational two-sequence DP.                                                                                          |
| #194 | LC 282: Expression Add Operators           | Hard       | Backtracking           | Medium           | Complex recursive state and arithmetic.                                                                                |
| #195 | LC 679: 24 Game                            | Hard       | Backtracking / math    | Medium           | Search over values/operations.                                                                                         |
| #196 | LC 93: Restore IP Addresses                | Medium     | Backtracking           | Medium           | Parsing plus bounded branching.                                                                                        |
| #197 | LC 1143: Longest Common Subsequence        | Medium     | DP                     | Medium           | Baseline two-string DP.                                                                                                |
| #198 | LC 64: Minimum Path Sum                    | Medium     | Grid DP                | Medium           | Basic matrix DP.                                                                                                       |
| #199 | LC 516: Longest Palindromic Subsequence    | Medium     | DP                     | Medium           | Interval/subsequence state.                                                                                            |
| #200 | LC 291: Word Pattern II                    | Medium     | Backtracking / hashing | Medium           | Bijective assignment with pruning.                                                                                     |
| #201 | LC 5: Longest Palindromic Substring        | Medium     | Expand-center / DP     | Medium           | Know O(n²) cleanly.                                                                                                    |
| #202 | LC 221: Maximal Square                     | Medium     | Grid DP                | Medium           | Compact local recurrence.                                                                                              |
| #203 | LC 647: Palindromic Substrings             | Medium     | DP / expand center     | Medium           | Useful palindrome primitive.                                                                                           |
| #204 | LC 741: Cherry Pickup                      | Hard       | Grid DP                | Medium           | High-value multi-agent/state DP, but expensive prep.                                                                   |
| #205 | LC 1463: Cherry Pickup II                  | Hard       | Grid DP                | Medium           | Cleaner multi-agent grid DP representative.                                                                            |
| #206 | LC 322: Coin Change                        | Medium     | DP                     | Medium           | Basic unbounded knapsack.                                                                                              |
| #207 | LC 931: Minimum Falling Path Sum           | Medium     | Grid DP                | Medium           | Straightforward row-state optimization.                                                                                |
| #208 | LC 518: Coin Change II                     | Medium     | DP                     | Medium           | Combination-order semantics.                                                                                           |
| #209 | LC 17: Letter Combinations of Phone Number | Medium     | Backtracking           | Medium           | You know it; use as a speed warm-up.                                                                                   |
| #210 | LC 416: Partition Equal Subset Sum         | Medium     | Knapsack DP            | Medium           | 0/1 subset-state baseline.                                                                                             |
| #211 | LC 85: Maximal Rectangle                   | Hard       | DP / monotonic stack   | Medium           | Connect matrix problem to histogram primitive.                                                                         |
| #212 | LC 494: Target Sum                         | Medium     | DP                     | Medium           | Transformation into subset-sum.                                                                                        |
| #213 | LC 377: Combination Sum IV                 | Medium     | DP                     | Medium           | Order-sensitive counting.                                                                                              |
| #214 | LC 362: Design Hit Counter                 | Medium     | Queue / streaming      | Medium           | Very relevant online-state API problem.                                                                                |
| #215 | LC 115: Distinct Subsequences              | Hard       | DP                     | Medium           | Counting two-sequence DP.                                                                                              |
| #216 | LC 337: House Robber III                   | Medium     | Tree DP                | Medium           | Tree-state DP.                                                                                                         |
| #217 | LC 97: Interleaving String                 | Medium     | DP                     | Medium           | 2D string-state reasoning.                                                                                             |
| #218 | LC 583: Delete Operation for Two Strings   | Medium     | DP                     | Medium           | LCS transformation.                                                                                                    |
| #219 | LC 712: Minimum ASCII Delete Sum           | Medium     | DP                     | Medium           | Weighted sequence alignment.                                                                                           |
| #220 | LC 91: Decode Ways                         | Medium     | DP                     | Medium           | Tiny-state DP with edge cases.                                                                                         |
| #221 | LC 639: Decode Ways II                     | Hard       | DP                     | Medium           | Hard combinatorial extension.                                                                                          |
| #222 | LC 62: Unique Paths                        | Medium     | DP                     | Medium           | Basic grid recurrence; solve instantly.                                                                                |
| #223 | LC 63: Unique Paths II                     | Medium     | DP                     | Medium           | Obstacle variant.                                                                                                      |
| #224 | LC 359: Logger Rate Limiter                | Easy       | Hash / streaming       | Medium           | Simple online-state problem with excellent follow-up potential.                                                        |
| #225 | LC 120: Triangle                           | Medium     | DP                     | Medium           | Space-reduction exercise.                                                                                              |
| #226 | LC 198: House Robber                       | Medium     | DP                     | Medium-Low       | Baseline state compression.                                                                                            |
| #227 | LC 213: House Robber II                    | Medium     | DP                     | Medium-Low       | Circular-state extension.                                                                                              |
| #228 | LC 312: Burst Balloons                     | Hard       | Interval DP            | Medium-Low       | Excellent interval-DP representative.                                                                                  |
| #229 | LC 664: Strange Printer                    | Hard       | Interval DP            | Medium-Low       | Difficult recurrence; good but lower expected value.                                                                   |
| #230 | LC 346: Moving Average from Data Stream    | Easy       | Queue / streaming      | Medium-Low       | Online bounded-window API baseline.                                                                                    |
| #231 | LC 1547: Minimum Cost to Cut a Stick       | Hard       | Interval DP            | Medium-Low       | Cleaner interval-DP training than many exotic Hards.                                                                   |
| #232 | LC 1000: Minimum Cost to Merge Stones      | Hard       | Interval DP            | Medium-Low       | Advanced interval-state constraints.                                                                                   |
| #233 | LC 486: Predict the Winner                 | Medium     | Game DP                | Medium-Low       | Minimax/score-difference DP.                                                                                           |
| #234 | LC 763: Partition Labels                   | Medium     | Greedy / intervals     | Medium-Low       | Compact greedy proof.                                                                                                  |
| #235 | LC 877: Stone Game                         | Medium     | Game DP                | Medium-Low       | Basic adversarial-state reasoning.                                                                                     |
| #236 | LC 25: Reverse Nodes in k-Group            | Hard       | Linked list            | Medium-Low       | Lower Google-specific evidence, but excellent pointer-invariant test.                                                  |
| #237 | LC 1140: Stone Game II                     | Medium     | Game DP                | Medium-Low       | Memoized game state.                                                                                                   |
| #238 | LC 2: Add Two Numbers                      | Medium     | Linked list            | Medium-Low       | Pointer baseline.                                                                                                      |
| #239 | LC 1406: Stone Game III                    | Hard       | Game DP                | Medium-Low       | Strong but relatively niche.                                                                                           |
| #240 | LC 1024: Video Stitching                   | Medium     | Greedy / intervals     | Medium-Low       | Interval-cover greedy.                                                                                                 |
| #241 | LC 307: Range Sum Query — Mutable          | Medium     | Fenwick / segment tree | Medium-Low       | Know at least one update/query structure well.                                                                         |
| #242 | LC 188: Best Time to Buy/Sell Stock IV     | Hard       | DP                     | Medium-Low       | Generic k-transaction state.                                                                                           |
| #243 | LC 309: Stock with Cooldown                | Medium     | DP                     | Medium-Low       | State-machine DP.                                                                                                      |
| #244 | LC 714: Stock with Transaction Fee         | Medium     | DP                     | Medium-Low       | State-machine variation.                                                                                               |
| #245 | LC 123: Stock III                          | Hard       | DP                     | Medium-Low       | Bounded transaction states.                                                                                            |
| #246 | LC 138: Copy List with Random Pointer      | Medium     | Linked list / hash     | Medium-Low       | Useful mutation/copy invariant.                                                                                        |
| #247 | LC 871: Minimum Refueling Stops            | Hard       | Greedy / heap          | Medium-Low       | Strong heap-greedy representative.                                                                                     |
| #248 | LC 502: IPO                                | Hard       | Greedy / heap          | Medium-Low       | Two-condition frontier + max-heap.                                                                                     |
| #249 | LC 766: Toeplitz Matrix                    | Easy       | Matrix / streaming     | Medium-Low       | Historically Google asked a version followed by "matrix doesn't fit in memory." ([LeetCode][13])                       |
| #250 | LC 630: Course Schedule III                | Hard       | Greedy / heap          | Medium-Low       | Deadline scheduling and replacement.                                                                                   |

---

# Tier D — #251–300: Lower probability / useful edge coverage

| Rank | Problem                                              | Difficulty | Primary Pattern         | Google Relevance | Why it is here                                                     |
| ---- | ---------------------------------------------------- | ---------- | ----------------------- | ---------------- | ------------------------------------------------------------------ |
| #251 | LC 122: Best Time to Buy/Sell Stock II               | Medium     | Greedy                  | Medium-Low       | Simple greedy proof.                                               |
| #252 | LC 55: Jump Game                                     | Medium     | Greedy                  | Medium-Low       | Reachability invariant.                                            |
| #253 | LC 45: Jump Game II                                  | Medium     | Greedy                  | Medium-Low       | Greedy BFS-layer interpretation.                                   |
| #254 | LC 134: Gas Station                                  | Medium     | Greedy                  | Medium-Low       | Global-vs-local feasibility proof.                                 |
| #255 | LC 135: Candy                                        | Hard       | Greedy                  | Medium-Low       | Two directional constraints.                                       |
| #256 | LC 327: Count of Range Sum                           | Hard       | Prefix sum / Fenwick    | Medium-Low       | Advanced range-counting.                                           |
| #257 | LC 659: Split Array into Consecutive Subsequences    | Medium     | Greedy / hash           | Medium-Low       | Greedy resource assignment.                                        |
| #258 | LC 846: Hand of Straights                            | Medium     | Greedy / ordered map    | Medium-Low       | Ordered counts.                                                    |
| #259 | LC 402: Remove K Digits                              | Medium     | Monotonic stack         | Medium-Low       | Greedy stack invariant.                                            |
| #260 | LC 316: Remove Duplicate Letters                     | Medium     | Monotonic stack         | Medium-Low       | Stack plus remaining-count invariant.                              |
| #261 | LC 330: Patching Array                               | Hard       | Greedy                  | Medium-Low       | Elegant proof but less likely than core mediums.                   |
| #262 | LC 853: Car Fleet                                    | Medium     | Stack / sorting         | Medium-Low       | Ordering + convergence.                                            |
| #263 | LC 406: Queue Reconstruction by Height               | Medium     | Greedy / sorting        | Medium-Low       | Non-obvious greedy ordering.                                       |
| #264 | LC 84: Largest Rectangle in Histogram                | Hard       | Monotonic stack         | Medium-Low       | Canonical monotonic-stack Hard.                                    |
| #265 | LC 304: Range Sum Query 2D — Immutable               | Medium     | 2D prefix sum           | Medium-Low       | Essential 2D prefix primitive.                                     |
| #266 | LC 739: Daily Temperatures                           | Medium     | Monotonic stack         | Medium-Low       | Simplest useful monotonic-stack rep.                               |
| #267 | LC 121: Best Time to Buy/Sell Stock                  | Easy       | Greedy                  | Medium-Low       | One-pass invariant.                                                |
| #268 | LC 503: Next Greater Element II                      | Medium     | Monotonic stack         | Medium-Low       | Circular stack handling.                                           |
| #269 | LC 901: Online Stock Span                            | Medium     | Monotonic stack         | Medium-Low       | Online stack state.                                                |
| #270 | LC 315: Count Smaller After Self                     | Hard       | Fenwick / merge sort    | Medium-Low       | Strong advanced ordering/counting problem.                         |
| #271 | LC 907: Sum of Subarray Minimums                     | Medium     | Monotonic stack         | Medium-Low       | Contribution counting.                                             |
| #272 | LC 54: Spiral Matrix                                 | Medium     | Matrix simulation       | Medium-Low       | Edge-case-heavy implementation.                                    |
| #273 | LC 493: Reverse Pairs                                | Hard       | Merge sort / Fenwick    | Medium-Low       | Modified merge sort.                                               |
| #274 | LC 48: Rotate Image                                  | Medium     | Matrix                  | Medium-Low       | In-place matrix manipulation.                                      |
| #275 | LC 73: Set Matrix Zeroes                             | Medium     | Matrix / in-place       | Medium-Low       | O(1)-space follow-up.                                              |
| #276 | LC 456: 132 Pattern                                  | Medium     | Monotonic stack         | Medium-Low       | Non-obvious reverse stack invariant.                               |
| #277 | LC 289: Game of Life                                 | Medium     | Matrix / in-place       | Medium-Low       | State encoding and space reduction.                                |
| #278 | LC 71: Simplify Path                                 | Medium     | Stack / parsing         | Medium-Low       | Parsing/API-adjacent baseline.                                     |
| #279 | LC 498: Diagonal Traverse                            | Medium     | Matrix simulation       | Medium-Low       | Index/state control.                                               |
| #280 | LC 150: Evaluate Reverse Polish Notation             | Medium     | Stack                   | Medium-Low       | Expression-evaluation baseline.                                    |
| #281 | LC 352: Data Stream as Disjoint Intervals            | Hard       | Ordered map / intervals | Medium-Low       | Online intervals with merge updates.                               |
| #282 | LC 224: Basic Calculator                             | Hard       | Stack / parsing         | Medium-Low       | Stateful parser.                                                   |
| #283 | LC 227: Basic Calculator II                          | Medium     | Stack / parsing         | Medium-Low       | Parsing baseline.                                                  |
| #284 | LC 856: Score of Parentheses                         | Medium     | Stack                   | Medium-Low       | Recursive/stack structural evaluation.                             |
| #285 | LC 2770: Maximum Number of Jumps to Reach Last Index | Medium     | DP                      | Medium-Low       | Additional state-DP practice.                                      |
| #286 | LC 735: Asteroid Collision                           | Medium     | Stack / simulation      | Medium-Low       | Collision state machine.                                           |
| #287 | LC 2390: Removing Stars From a String                | Medium     | Stack                   | Medium-Low       | Easy stack warm-up.                                                |
| #288 | LC 496: Next Greater Element I                       | Easy       | Monotonic stack         | Medium-Low       | Fundamental next-greater primitive.                                |
| #289 | LC 277: Find the Celebrity                           | Medium     | Elimination             | Medium-Low       | You've practiced it; useful mainly for elimination-proof thinking. |
| #290 | LC 287: Find the Duplicate Number                    | Medium     | Cycle detection         | Medium-Low       | Floyd's algorithm in a non-linked-list setting.                    |
| #291 | LC 772: Basic Calculator III                         | Hard       | Parsing / recursion     | Medium-Low       | Full expression parser; lower frequency but good synthesis.        |
| #292 | LC 92: Reverse Linked List II                        | Medium     | Linked list             | Medium-Low       | Pointer mutation.                                                  |
| #293 | LC 142: Linked List Cycle II                         | Medium     | Two pointers            | Medium-Low       | Floyd cycle-entry proof.                                           |
| #294 | LC 622: Design Circular Queue                        | Medium     | Queue / design          | Medium-Low       | API + ring-buffer indexing.                                        |
| #295 | LC 641: Design Circular Deque                        | Medium     | Deque / design          | Medium-Low       | Ring-buffer/state design.                                          |
| #296 | LC 19: Remove Nth Node From End                      | Medium     | Linked list             | Medium-Low       | Two-pointer baseline.                                              |
| #297 | LC 20: Valid Parentheses                             | Easy       | Stack                   | Medium-Low       | Warm-up only.                                                      |
| #298 | LC 143: Reorder List                                 | Medium     | Linked list             | Medium-Low       | Several pointer techniques combined.                               |
| #299 | LC 911: Online Election                              | Medium     | Prefix / binary search  | Medium-Low       | Precomputation + historical queries.                               |
| #300 | LC 430: Flatten Multilevel Doubly Linked List        | Medium     | Linked list / DFS       | Medium-Low       | Pointer-heavy structural traversal.                                |

That is **exactly 300 unique entries**, including 10 high-value recent reported variants rather than pretending every useful Google question maps exactly to LeetCode.

---

# 1. Pattern distribution

I classified each problem by its dominant learning pattern rather than trying to make the buckets artificially equal.

| Major pattern                                    |  Count |
| ------------------------------------------------ | -----: |
| Dynamic programming                              | **49** |
| Trees / BST                                      | **36** |
| Graphs / topological sort / shortest paths / DSU | **35** |
| Stacks / monotonic stacks                        | **23** |
| Heaps / priority queues                          | **18** |
| Backtracking                                     | **18** |
| Intervals / sweep line                           | **17** |
| Arrays / math / DS design / other                | **16** |
| Binary search                                    | **15** |
| Greedy                                           | **11** |
| Matrices / grids                                 | **10** |
| Prefix sums / range queries                      | **10** |
| Tries                                            |  **9** |
| Linked lists                                     |  **8** |
| Randomization / sampling                         |  **7** |
| Sliding window                                   |  **7** |
| Hash maps / sets                                 |  **7** |
| Iterators                                        |  **3** |
| Parsing/string-primary                           |  **1** |

Don't interpret the 49 DP entries as "16% chance your question is DP." Many problems classified elsewhere also use DP/memoization, while many of the DP problems live in Tiers C/D.

The **top 100 distribution is much more important**: graphs, topo sort, intervals/sweep, heaps/streaming, tries, prefix sums, randomization and stateful data structures dominate. That's consistent with recent L5 experiences describing graph/grid problems, interval scheduling, stream optimization, randomization, Range Module and matrix/topological problems. ([LeetCode][1])

---

# 2. Difficulty distribution

Across the 300:

* **Easy: 12 — 4.0%**
* **Medium: 211 — 70.3%**
* **Hard: 77 — 25.7%**

That's intentional.

A recent Mountain View report described the three coding rounds as **two Mediums and one Medium-Hard**, while a September 2026 Google-prep discussion from candidates doing mocks with Google engineers describes the target as essentially medium-to-hard LeetCode wrapped in real-world language. L5 reports sometimes contain genuine Hards, especially DP, but mastering Mediums rapidly and extending them under follow-ups has better expected value than grinding obscure Hards. ([Jointaro][14])

---

# 3. The 30 I would repeat until blank-screen automatic

These aren't simply #1–30 because I want **pattern diversity** rather than rehearsing five interval variants.

1. Alien Dictionary
2. Meeting Rooms III
3. Range Module
4. Build a Matrix With Conditions
5. Insert Delete GetRandom O(1)
6. Evaluate Division
7. Course Schedule II
8. Word Ladder
9. Find Median from Data Stream
10. Network Delay Time
11. Longest Increasing Subsequence
12. The Maze II
13. Accounts Merge
14. Longest Increasing Path in a Matrix
15. Minimum Interval to Include Each Query
16. Subarray Sum Equals K
17. Sliding Window Maximum
18. Minimum Window Substring
19. Kth Largest Element in an Array
20. Design In-Memory File System
21. Time Based Key-Value Store
22. Random Pick with Weight
23. Random Pick Index / reservoir sampling
24. Split Array Largest Sum
25. Serialize and Deserialize Binary Tree
26. Binary Tree Maximum Path Sum
27. Word Search II
28. Edit Distance
29. Regular Expression Matching
30. **Worker Shift Timeline reported variant**

For each, your target shouldn't be "I remember the solution." It should be: **derive it, explain brute force, identify the invariant/state, implement cleanly, test it, give complexity, and survive one changed constraint in ~30–35 minutes.**

---

# 4. What appears distinctive about Google coding interviews

The most important difference is that **Google appears more willing than Meta to hide the underlying pattern behind an unfamiliar formulation**. A recent Google interviewer specifically warned that simply being good at LeetCode isn't enough because candidates must articulate choices to an interviewer and respond productively to guidance. Recent interview reports similarly mention intentionally vague or real-world problem statements. ([Reddit][15])

Compared with **Meta**, I'd spend somewhat less time trying to achieve near-instant recognition of a relatively compact tagged set, and more time deriving unfamiliar graph/DP/interval problems and handling follow-ups.

Compared with **LinkedIn**, your previous preparation transfers well—particularly graphs, topological sort and design-oriented data structures—but I'd shift substantially more effort toward **DP, randomized algorithms, sweep-line/interval mutations, tricky graph modeling, streaming questions and ambiguous follow-ups**.

Compared with **Amazon**, I'd expect less emphasis on straightforward implementation of common patterns and relatively more emphasis on algorithmic reframing/proofs and progressive follow-ups.

For **L5 specifically**, the coding algorithm isn't necessarily harder merely because you're senior. The stronger senior signal comes from being disciplined about API assumptions, extensibility, complexity, testability and what changes when the dataset no longer fits on one machine. L5 anecdotes include distributed follow-ups even inside coding/design-style questions. ([LeetCode][6])

---

# 5. Senior-level follow-ups to rehearse

For Tier S/A, after solving the ordinary problem, deliberately ask yourself one of these:

* **"The input no longer fits in memory."** Toeplitz Matrix, file-system traversal, merge streams, graphs. Google has explicitly used this follow-up style. ([LeetCode][13])
* **"Input becomes a stream."** Median, top-k, intervals, random sampling, logger/hit counter.
* **"Updates are now supported."** Prefix sums → Fenwick/segment tree; static intervals → Range Module/My Calendar.
* **"Queries vastly outnumber writes."** Discuss precomputation/storage tradeoffs.
* **"Writes vastly outnumber queries."** Invert the optimization.
* **"Make the API thread-safe."** Caches, queues, rate limiters, randomized structures.
* **"Run this distributed."** DSU/connectivity and range/query problems have appeared with exactly this kind of L5 extension. ([LeetCode][6])
* **"Return the actual path/sequence, not only its length/cost."** LIS, DP, shortest path, tree DP.
* **"Return all optimal answers."** Explodes output size; discuss output-sensitive complexity.
* **"Edges/intervals arrive incrementally."** Connectivity, calendars, shortest-path maintenance.
* **"Delete is now allowed."** Trie, DSU, interval sets, caches.
* **"Reduce O(n) extra memory to O(1) or O(width)."** Matrix DP, linked lists, parsing.
* **"Generalize from 2D to N dimensions."** Geometry/grid/state encoding.
* **"What if there are billions of nodes?"** Sparse adjacency, external memory, partitioning.
* **"Prove it."** Greedy, binary search, monotonic stacks, reservoir sampling.
* **"What if input is adversarial?"** Hash collisions, recursion depth, worst-case quickselect.
* **"Can you expose this as a reusable class/API?"** Range Module, calendar, iterator, trie, cache.
* **"What if requests are concurrent?"** Lock granularity, atomicity and consistency.
* **"How would you test this?"** Empty input, duplicate values, overflow, boundaries, disconnected graph, cycles, one-element cases.

I would practice these aloud, because multiple L5 reports show that the *follow-up*, not necessarily the initial problem, was where candidates lost the round. ([LeetCode][7])

---

# 6. Evidence quality and sources

### Stronger / directly relevant evidence

Recent **Google L5/Senior interview accounts** were the most heavily weighted inputs. A January 2025 L5 report includes the worker-shift sweep problem, tree-root/color problem and Range Module. Another L5 report includes Build a Matrix With Conditions. Other L5 accounts include stream optimization, hard DP/randomization, grid traversal, file-directory compression and heap-driven follow-ups. ([LeetCode][1])

For your ML-specific role, I also weighted the Google MLE evidence: an L6 MLE loop reported two coding rounds including a logger/timer problem with repeatedly added constraints and an optimized grid problem. That's only one anecdote, but the **incremental-constraint style** is consistent with the L5 evidence. ([LeetCode][11])

Bay Area evidence received only a small bonus. One Bay Area L5 report had regex-style backtracking, Exclusive Time, an Earliest Moment/DSU variant and an Insert/Delete/GetRandom-style question, including distributed and complexity follow-ups. ([LeetCode][6])

### Aggregated evidence

I used public repositories that mirror LeetCode company tags as **supporting evidence**, not ground truth. The large liquidslr repository says its files are based on LeetCode company tags and include 30/60/90-day and all-time windows; other repositories were updated into 2026. Those lists are useful but are subject to reporting bias, stale tagging and duplicates, hence they did not dictate the rankings. ([GitHub][2])

Interview Query's current Google SWE guide independently characterizes Google interviews as coding-heavy and notes graph traversal, DP, optimization and follow-ups in L5 accounts. 

Glassdoor has much noisier question data, but a June 2025 Senior SWE report from San Francisco described an AI-oriented loop whose coding was "mostly Google tagged," while another specifically mentioned a sliding-window coding round. ([Glassdoor][16])

### Anecdotal / lower confidence

Reddit and LeetCode Discuss reports are self-reported and cannot be treated as verified Google question banks. I used them primarily to infer **style and recurring patterns**, not numerical frequencies. Particularly useful were the 2026 Google interviewer post and recent L5/Google-prep discussions. ([Reddit][15])

So I have **high confidence in the Tier-S/A pattern distribution**, moderate confidence in the relative ordering within roughly ±10–20 places, and very low confidence in any claim such as "problem X has a 4.3% probability." The available data simply doesn't justify that kind of precision.

### What I'd do with your prep time

Given your October interview, I would **not attempt all 300 once**. I'd go **#1–50 deeply → #51–100 deeply → repeat the Top 30 → #101–175 selectively → only then #176–300**. For Google, solving 100 problems with proper follow-up simulation is much more valuable than superficially completing 300.

And because you've already done Course Schedule II, Number of Islands, LRU, Nested Iterator, Celebrity, K Closest, N-ary diameter, Word Ladder, N-Queens, All O(1), etc., I would use those mostly as **15-minute revision checkpoints**, freeing your main study time for the Google-heavy gaps above.

[1]: https://leetcode.com/discuss/post/6522571/google-l5-interview-january-2025-by-anon-v92c/?utm_source=chatgpt.com "Google L5 Interview | January 2025 - Discuss - LeetCode"
[2]: https://github.com/liquidslr/leetcode-company-wise-problems/?utm_source=chatgpt.com "GitHub - liquidslr/leetcode-company-wise-problems: Lists of company wise questions. Every csv file in the companies directory corresponds to a list of questions on leetcode for a specific company based on the leetcode company tags. Updated as of 20 June, 2025 · GitHub"
[3]: https://leetcode.com/discuss/post/6675591/timeline-for-google-interview-2025-by-an-kouh/?utm_source=chatgpt.com "Timeline for Google interview 2025 - Discuss - LeetCode"
[4]: https://leetcode.com/discuss/post/7631077/?utm_source=chatgpt.com "Extremely sad Google L5 interview experience - Discuss - LeetCode"
[5]: https://leetcode.com/discuss/post/6782644/google-l5-interview-experience-by-anonym-p4xu/?utm_source=chatgpt.com "Google L5 Interview Experience - Discuss - LeetCode"
[6]: https://leetcode.com/discuss/post/2559774/Google-or-L5or-Bay-Area-or-Phone-Screen-and-Onsite/?utm_source=chatgpt.com "Google | L5| Bay Area | Phone Screen and Onsite - Discuss - LeetCode"
[7]: https://leetcode.com/discuss/post/5601424/Google-L5-Interview-Experience/?utm_source=chatgpt.com "Google L5 Interview Experience - Discuss - LeetCode"
[8]: https://leetcode.com/discuss/post/7101066/google-interview-experience-trie-questio-6d7r/?utm_source=chatgpt.com "Google Interview Experience ( Trie Question ) - Discuss - LeetCode"
[9]: https://leetcode.com/discuss/post/7371064/?utm_source=chatgpt.com "Google Software Engineer, University Graduate, 2026 - India — Interview Experience (DSA+Googlyness) - Discuss - LeetCode"
[10]: https://leetcode.com/discuss/post/4820834/Google-L5-SSE-interview-experience/?utm_source=chatgpt.com "Google L5 SSE interview experience - Discuss - LeetCode"
[11]: https://leetcode.com/discuss/post/6010240/Google-MLEor-L6or-Interview-Experience-and-Resources-for-preparation/?utm_source=chatgpt.com "Google MLE| L6| Interview Experience and Resources for preparation - Discuss - LeetCode"
[12]: https://leetcode.com/discuss/post/6072539/?utm_source=chatgpt.com "Google Elimination Round Interview Experience - Discuss - LeetCode"
[13]: https://leetcode.com/discuss/post/124626/google-onsite-interview-questions/?utm_source=chatgpt.com "Google | Onsite interview questions - Discuss - LeetCode"
[14]: https://www.jointaro.com/interviews/companies/google/experiences/software-engineer-mountain-view-ca-june-30-2025-no-offer-positive-c24628e2/?utm_source=chatgpt.com "Google Software Engineer Interview Experience - Mountain View, California"
[15]: https://www.reddit.com/r/leetcode/comments/1ts0hab/what_leetcode_doesnt_teach_you_from_a_google/?utm_source=chatgpt.com "What Leetcode doesn't teach you (from a Google interviewer with 10 YOE)"
[16]: https://www.glassdoor.com/Interview/Google-Senior-Software-Ebgineer-Interview-Questions-EI_IE9079.0%2C6_KO7%2C31.htm?utm_source=chatgpt.com "Google Senior Software Ebgineer Interview Questions | Glassdoor"
