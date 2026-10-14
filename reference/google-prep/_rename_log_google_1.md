graph_topo_coursescheduleii.png | 210. Course Schedule II | Kahn's BFS topological sort with indegrees to return a valid course order; empty if cycle.
design_twostacks_designatexteditor.png | 2296. Design a Text Editor | Text editor with cursor using left/right stacks; add, delete, move cursor returning last 10 chars.
heap_twoheaps_findmedianfromdatastream.png | LeetCode 295. Find Median from Data Stream | Max-heap lower half + min-heap upper half, rebalance on add; median from heap tops.
string_hamming_wordswithintwoeditsofdictionary.png | 2452. Words Within Two Edits of Dictionary | Brute-force mismatch counting (Hamming distance <= 2) per query vs dictionary; bonus trie DFS.
tree_xor_findrootofnarytree.png | Find Root of N-ary Tree | XOR all node and child values so root survives (O(1) space); alt set of children.
design_bucket_loosemediandatastructure.png | Loose Median Data Structure | 64 power-of-2 buckets keyed by bit_length; scan cumulative counts to find median bucket, return 2^k.
unionfind_dsu_accountsmerge.png | LeetCode 721. Accounts Merge | Union-find over emails, group by root, sort emails and prepend owner name.
twopointers_greedy_swapadjacentinlrstring.png | Swap Adjacent in LR String (String Transformation) | Two pointers skip X; non-X order must match, L may only move left and R only right.
graph_dfs_evaluatedivision.png | 399. Evaluate Division | Weighted bidirectional graph (k and 1/k); DFS path product answers each query, -1.0 if none.
design_hashmap_loggerratelimiter.png | Logger Rate Limiter | Hash map message -> next allowed timestamp; print if timestamp >= next_allowed, set to t+10.
graph_retrogradebfs_catandmouse.png | LeetCode 913. Cat and Mouse | Game theory over (mouse, cat, turn) states; reverse BFS from terminal states with degree counting.
hashing_normalize_groupshiftedstrings.png | Group Shifted Strings | Normalize each string so first char is 'a' (mod 26) and group by that key; alt diff-tuple key.
unionfind_dsu_earliestacquaintancetime.png | Earliest Acquaintance Time (Union Find / DSU) | Sort logs by time, union friends tracking component count; return time when components == 1.
design_slidingwindow_designaratelimiter.png | Design a Rate Limiter | Thread-safe sliding-window limiter: deque of timestamps in last 1000 ms guarded by a Lock.
trie_dfs_designaddandsearchwordsdatastructure.png | 211. Design Add and Search Words Data Structure | Trie insert; search via DFS where '.' wildcard tries all children.
design_trie_designinmemoryfilesystem.png | Design In-Memory File System | Trie of path components (FileNode with children/is_file/content) supporting mkdir, ls, add/read file.
design_ordereddict_lfucache.png | LFU Cache (LeetCode 460) | O(1) LFU via key->(val,freq), freq->OrderedDict buckets and min_freq; LRU tie-break on eviction.
tree_degree_findrootthatmakesgraphbinarytree.png | Find a Root That Makes the Graph a Binary Tree | Root must have degree <= 2; follow-ups with B/W alternating colors and R/B/W cycle via edge orientation/indegree.
graph_dfs_numberofclosedislands.png | 1254. Number of Closed Islands | Flood-fill boundary-connected land with DFS, then count remaining 0-islands in the interior.
heap_topk_findtop5largestfilesindirectorytree.png | Find Top 5 Largest Files in a Directory Tree | DFS the directory tree via list_dir/size_of, keep a size-5 min-heap of (size, path), return sorted desc.
trie_frequency_designautocompletesystem.png | Design Autocomplete System | Trie nodes store sentences + frequency map; input(c) walks trie, returns top 3 by (-freq, sentence); '#' commits.
unionfind_dsu_pathwithmaximumminimumvalue.png | Maximum Minimum Path (Alternative Solution: DSU / Union-Find) | Activate cells high to low, union active neighbors; first value connecting start and end is the answer.
string_formatting_formatnumberwithxsignificantdigits.png | Format Number with X Significant Digits | Split on '.', truncate to X digits (zero-pad integer part if needed), add thousand separators.
hashing_groupby_friendrecommendations.png | Friend Recommendations (Python) | Dedupe listens, group users by (day, song), count shared songs per user pair/day, keep >=3 and exclude existing friends.
graph_dfs_floodfill.png | 733. Flood Fill | 4-directional DFS recolor of cells matching original color; return early if color already equal.
prefixsum_differencearray_carpooling.png | 1094. Car Pooling | Difference array +p at start, -p at end; sweep running sum and fail if it exceeds capacity.
design_quickselect_filesystemsizeanalysis.png | File System Size Analysis and Reporting | Trie of paths with total/immediate sizes via DFS; getSize plus k largest files/folders via quickselect.
graph_dfs_pacificatlanticwaterflow.png | 417. Pacific Atlantic Water Flow | Reverse multi-source DFS from each ocean's borders climbing to >= heights; answer is intersection.
intervals_segmenttree_rangemodule.png | Range Module — Last-Minute Revision | Add/query/remove half-open ranges via sorted disjoint interval list, or dynamic segment tree with lazy propagation.
heap_twoheaps_slidingwindowmedian.png | 480. Sliding Window Median | Two heaps with lazy deletion hashmap and size balancing to report median of each size-k window.
graph_topo_aliendictionary.png | Alien Dictionary | Edges from first differing char of adjacent words, Kahn's topo sort; invalid prefix or cycle returns empty.
greedy_counting_taskscheduler.png | 621. Task Scheduler – Revision Card | Formula max(len(tasks), (f-1)*(n+1)+k) using max frequency f and count k of most frequent tasks.
intervals_greedy_minimumnumberofarrowstoburstballoons.png | 452. Minimum Number of Arrows to Burst Balloons | Sort by end, shoot at earliest end, reuse arrow while start <= arrow_pos; new arrow otherwise.
graph_dfs_countsubislands.png | 1905. Count Sub Islands | DFS each grid2 island, checking every cell is land in grid1; explore fully before counting.
queue_slidingwindow_movingaveragefromdatastream.png | Moving Average from Data Stream | Deque of last k values with running sum; pop oldest when over k, return sum/len in O(1).
graph_topo_sequencereconstruction.png | Sequence Reconstruction | Kahn's topo sort over adjacent-pair edges; unique iff queue size is always 1 and order equals nums.
intervals_merge_finduncoveredrangesinarray.png | Find Uncovered Ranges in an Array | Sort ranges by start, track first uncovered position, emit gaps before each range and a final tail gap.
intervals_sweepline_separatesquaresii_card1.png | LeetCode 3454 — Separate Squares II (Revision Card 1: Full Python Algorithm) | Sweep y-events with coordinate-compressed segment tree for union x-length; find y where area below = total/2.
unionfind_dsu_countalienpairsfromdifferentplanets.png | Count Alien Pairs from Different Planets | Union-find components (planets) by size; count cross-component pairs via running remaining or total minus same-planet.
