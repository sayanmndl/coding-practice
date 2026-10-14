string_runlength_stringcompression.png | Run-Length Encoding (String Compression) | Single pass counting consecutive chars, append char+count; O(N) time
trie_pathsegment_httproutematching.png | HTTP Route Matching - Revision Card | Router via segment trie with static children + one param child; static match before param, DFS backtracking
tree_postorder_deletenodesandreturnforest.png | 1110. Delete Nodes And Return Forest | Postorder DFS with is_root flag; non-deleted children of deleted nodes become new roots; O(n)
recursion_recursivedescent_evaluatenestedexpressions.png | Evaluate Nested Mathematical Expressions | Recursive descent parser with global index for add/sub/mul/div functional notation; O(n) time, O(depth) space
heap_topk_topkchatcontributors.png | Find Top K Chat Contributors | Counter + size-k min-heap, pop for ascending (reverse) order; nlargest alternative; O(N + U log k)
design_iterator_rleiterator.png | RLE Iterator (LeetCode 900) | Pointer over (count,value) pairs; next(n) consumes runs, decrementing counts in place; O(runs) total
dp_lis_longestincreasingsubsequence.png | LeetCode 300. Longest Increasing Subsequence | Patience sorting tails array + bisect_left, O(n log n); O(n^2) DP alternative
tree_dfs_binarytreeislands.png | Binary Tree Islands (Count & Sizes) | Single-pass DFS with parent_is_one flag; new island starts at a 1 whose parent is 0/None; collect sizes; O(n)
intervals_sweepline_minimumintervaltoincludeeachquery.png | LeetCode 1851. Minimum Interval to Include Each Query | Sort intervals and queries; sweep with min-heap of (size,right), pop expired; O((N+Q) log N)
hashing_counting_senderwithlargestwordcount.png | 2284. Sender With Largest Word Count | Hashmap sender->word count via split; pick max with lexicographically-largest tie-break; O(T)
tree_dfs_binarytreevalueislands.png | Binary Tree Value Islands - Revision Card | Same-value connected components via parent-child edges; new island when value differs from parent; counts by value and sizes; O(N)
trie_ahocorasick_multipatternstringreplacement.png | Multi-Pattern String Replacement - Trie + Aho-Corasick | Trie + BFS fail links + output inheritance; scan once, keep longest whole-word match per start, rebuild string; O(N+M+Z)
array_sentinel_missingranges.png | Missing Ranges - Revision Card: One-Pass Sentinel Solution | One pass with prev=lower-1 and virtual upper+1 sentinels; emit [prev+1,curr-1] when gap >1; O(n)
unionfind_nextpointer_rangeassignmentqueries.png | Range Assignment Queries on an Array | Constant K: difference array; varying K: process queries backwards with DSU next-unprocessed pointer; O(N+Q)
heap_sweepline_skylineproblem.png | LeetCode 218. The Skyline Problem | Start/end events sorted by x, sweep with lazy-deletion max-heap of (-h,right); emit key point on max change; O(N log N)
unionfind_cycledetection_redundantconnection.png | 684. Redundant Connection | DSU with path compression + union by rank; first edge whose endpoints share a root is redundant; O(n α(n))
array_runlength_adjacentincreasingsubarraysdetection2.png | 3350. Adjacent Increasing Subarrays Detection II | Track prev/curr increasing run lengths; ans=max(curr//2, min(prev,curr)) at each run end; O(n), O(1)
stack_matching_validparentheses.png | Valid Parentheses | Stack of openers with closing->opening map; mismatch or leftover means invalid; O(n)
graph_multisourcebfs_rottingoranges.png | 994. Rotting Oranges | Multi-source BFS from all rotten cells, level = minute, track fresh count; -1 if any remain; O(mn)
trie_backtracking_wordsearch2.png | 212. Word Search II | Trie of words + DFS backtracking from each cell, prune non-prefixes, mark visited, null out found words
design_lazypropagation_stackwithincrementoperation.png | 1381. Design a Stack With Increment Operation | Parallel lazy inc array; increment marks inc[min(k,size)-1], pop applies and propagates down; all ops O(1)
intervals_overlap_mycalendar2.png | 731. My Calendar II | Keep bookings and double-booked overlaps lists; reject if new event hits an overlap, else add intersections; O(n) per book
twopointers_opposite_twosum2inputarrayissorted.png | Two Sum II: Input Array Is Sorted (LeetCode 167) | Left/right pointers on sorted array, move by sum vs target, return 1-based indices; O(n), O(1)
heap_topk_movierecommendationsystem.png | Movie Recommendation System - Revision Card | Weighted content similarity (genres, cast, director, rating diff) + size-K min-heap with id tie-break; O(N log K)
slidingwindow_fixed_repeateddnasequences.png | 187. Repeated DNA Sequences | Fixed size-10 window with seen/repeated sets (bitmask rolling hash optional); O(n)
heap_greedymatching_processorderspartialfulfillment.png | Process Orders with Partial Fulfillment | Min-heap of Fizz supply by cost; each Buzz pops cheapest, partial match, push back remainder; O((n+k) log n)
greedy_linefill_numberoflinestowritestring.png | 806. Number of Lines To Write String | Greedily fill 100px lines with per-letter widths, new line on overflow; return [lines, last width]; O(n)
graph_dijkstra_themaze2.png | Maze (Shortest Distance with Rolling Ball) | Dijkstra over stopping positions; roll each direction until wall, edge weight = steps; O(mn(m+n) log mn)
intervals_greedy_nonoverlappingintervals.png | 435. Non-overlapping Intervals | Sort by end, greedily keep if start >= prev_end, count removals; O(n log n)
dp_memo_longestincreasingpathinamatrix.png | 329. Longest Increasing Path in a Matrix | Memoized DFS from every cell to strictly larger neighbors (DAG, no cycles); O(m*n)
heap_twoheaps_meetingrooms3.png | 2402. Meeting Rooms III | Sort by start; available-rooms heap + busy (end,room) heap, delay meetings when none free; count per room; O(m log m + m log n)
matrix_slotscan_checkifwordcanbeplacedincrossword.png | Check if Word Can Be Placed In Crossword | Scan maximal #-bounded row/column slots; match exact length against word or its reverse; O(m*n)
intervals_sweepline_mycalendar3.png | LeetCode 732. My Calendar III | Difference map +1/-1 at start/end, prefix-sum over sorted times for max active k; O(n log n) per booking
intervals_merge_insertinterval.png | 57. Insert Interval | Three-phase linear scan: add intervals before, merge overlapping into newInterval, add rest; O(n)
graph_hierholzer_reconstructitinerary.png | 332. Reconstruct Itinerary | Eulerian path via Hierholzer's: min-heap adjacency for lexical order, postorder append, reverse; O(E log E)
stack_callstack_exclusivetimeoffunctions.png | 636. Exclusive Time of Functions | Call stack of function ids + prev_time; credit top on start, inclusive +1 on end, caller resumes at ts+1; O(m)
intervals_overlap_mycalendar1.png | 729. My Calendar I | List of bookings; reject if s1<e2 and e1>s2 (half-open, touching allowed); O(n) per book
