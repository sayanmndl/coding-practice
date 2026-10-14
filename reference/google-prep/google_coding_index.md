# Coding revision cards — index

Your Freeform coding boards, named `<topic>_<technique>_<title>.png`. For one-at-a-time revision, use **▶ Card viewer** (Coding → Overview).

> ⚠️ Errors found on cards (49) — the card viewer shows these inline:
>
> - `backtracking_counting_generateparentheses` — Walkthrough tree has invalid/mismatched states (e.g. open=1,close=2 '())', open=3,close=2 '(()'); complexity should be O(4^n/sqrt(n)), not 4^n/sqrt(pi).
> - `backtracking_dfs_combinationsum` — Tree node 'exclude 2' under [2,2] is labeled [2,3] total=4; should be [2,2] (and [2,2,3]=7 is its success branch).
> - `backtracking_dfs_wordsearch_v2` — Example 2 path (0,3)E->(1,3)S->(2,3)E spells 'ESE'; the 'SEE' path is (1,3)S->(2,3)E->(2,2)E.
> - `backtracking_sets_nqueens` — Diagonal labels swapped: r-c constant is the top-left-to-bottom-right diagonal, r+c constant is top-right-to-bottom-left (visualization colors also mislabeled).
> - `backtracking_swap_permutations` — Walkthrough tree leaf under [1,2,3] after swap(1,2) shows [2,1,2]; should be [1,3,2].
> - `binarysearch_answer_aggressivecows` — Walkthrough d=4: greedy places at 0, 4, 9 (card says 10). Code returns False for k=1 (count==k only checked in loop). Complexity is O(n log n + n·log(max−min)).
> - `binarysearch_answer_kokoeatingbananas` — Code uses math.ceil without import math (or use (p + k - 1) // k).
> - `binarysearch_answer_splitarraylargestsum` — Card labels it 309 — it's LC 410. Step 4 'return low (or high)': only low/left is correct (the code does return left).
> - `binarysearch_partition_medianoftwosortedarrays` — Card labels it 27 — it's LC 4.
> - `bitmanip_fulladder_sumoftwointegers` — The carry line 'carry = (a_bit + b_bit + carry) >= 2' uses +, which the problem forbids. Use carry = (a_bit & b_bit) | (carry & (a_bit ^ b_bit)) instead. Rest of the logic (32-bit mask, ~(res ^ mask) for negatives) is fine.
> - `bst_lca_lowestcommonancestorofabinarysearchtree` — Typo: method name 'lowestCommonAnestor' — must be lowestCommonAncestor.
> - `design_hashmapdll_lrucache` — Walkthrough list order is wrong: after get(1) it should be 1:1 ⇄ 2:2; after put(3,3) (evicts 2) it should be 3:3 ⇄ 1:1. Map contents are right.
> - `dp_interval_burstballoons` — Code is right (the r loop could start at l instead of 1; when r<l the inner loop just does nothing). The DP trace table shows dp[1][1] = 1, but it should be 5 (1*1*5), which matches the box underneath it.
> - `dp_knapsack_coinchange2` — 2D code bug: dp[i][a] = dp[i+1][a] only runs inside 'if a >= coins[i]', so when a < coins[i] the skip-coin count is lost. It happens to work only because of coins.sort(), so the comment 'optional, not required' is wrong. Fix: always set dp[i][a] = dp[i+1][a], then add dp[i][a-coins[i]] if a >= coins[i]. The DP trace table is also wrong: the [2,5] row should be 1,0,1,0,1,1 and the [1,2,5] row 1,1,2,2,3,4. The 1D version is correct.
> - `dp_knapsack_coinchange_v2` — Code is correct; DP trace table has wrong per-coin candidate cells (e.g. a=6 coin 2 should be 3, a=7 coin 2 should be 2, a=8 coin 2 should be 3, a=11 coin 2 should be 4). The dp[a] min column and final answer 3 are right.
> - `dp_lastposition_minimumwindowsubsequence` — Card is wrong both ways: dry run 'bdde', stated 'bde'. Correct LC 727 answer for S='abcdebdde', T='bde' is 'bcde'.
> - `dp_memo_longestincreasingpathinamatrix_v2` — Example 1 explanation and arrows are wrong: 2->6->8->9 is not a path (8 is not adjacent to 6 at (1,0)), and the drawn arrows go 2->1 (decreasing). Correct longest path is 1->2->6->9. Code is correct.
> - `dp_statemachine_besttimetobuyandsellstockwithcooldown` — Code is right. The walkthrough table has wrong numbers from day 2 down: day 2 sell = 3 + dp[4][buy] = 3 + 0 = 3 (card says 3+2=5), so dp[2][hold]=3, dp[1][hold]=4, dp[1][buy]=2, and day 0 buy = -1+4 = 3. The final answer 3 is still correct.
> - `dp_tabulation_decodeways` — Space-optimized version initializes prev2, prev1 = 1, 0, so it returns 0 for every input (e.g. '12'). prev1 is dp[n] and must start at 1: use prev2, prev1 = 0, 1. The dict-based DP version is correct.
> - `dp_tabulation_distinctsubsequences` — Code is right, but Example 1 is misprinted: s should be 'rabbbit' (three b's), not 'rabbit' — with s = t = 'rabbit' the answer would be 1, not 3. The DP trace table doesn't match the real dp for s='rabbbit', t='rabbit' either (e.g. once s[i:] is shorter than t[j:] the value must be 0, but the table shows 1s and 3s). Trust the recurrence, not the table.
> - `dp_tabulation_editdistance` — Code is right. The DP table for 'horse'/'ros' is garbled: it lists only rows h,o,r,s (the 'e' row is missing, m should be 5), column 2 is labeled twice, and the n column is empty. dp[0][0]=3 is still the correct answer.
> - `dp_tabulation_houserobber1and2` — House Robber II helper has typo 'return nams[0]' (NameError) — should be nums[0]. 'Two cases' panel is wrong: nums[1:]=[2,3,1] max is 3 (2+1 or 3), not 4 'rob 2 and 3' (adjacent). Example 2 explanation should be houses 0 and 2 (1+3=4), not houses 1 and 3. Final answer 4 is right.
> - `graph_bfs_graphvalidtree` — Code typos 'whlie' and 'contiume' (should be while/continue).
> - `graph_dfs_maxareaofisland` — Island 2 in the example grid ((3,1),(4,1)) has area 2, not 3.
> - `graph_dfs_surroundedregions` — Example 2 is wrong: the inner O region touches the border O at (4,3) so it should not be captured (and input shows 'T' instead of 'O').
> - `graph_dijkstra_pathwithmaximumminimumvalue` — Stray ':' after `len(grid[0])` — remove it.
> - `graph_multisourcebfs_wallsandgates` — Stray ':' after `q.popleft()` — remove it.
> - `graph_multisourcebfs_wallsandgates_v2` — Code bug: 'grid[r][c] == dist' should be assignment '='; also final grid bottom row should be 0,-1,3,4 (card shows 0,-1,1,2) and (1,1) is 2 not 1 at the dist=1 step.
> - `graph_topo_courseschedule` — Code bugs: 'q.appeed(n)' typo and 'indegree[nei] += 1' should be '-= 1'.
> - `graph_topo_courseschedule2` — Import typo 'defaduldict' (should be defaultdict); the dry run adds course 3 to the queue one step early.
> - `greedy_counting_handofstraights` — Code bug: 'start ++ 1' is a no-op expression in Python (infinite loop); must be 'start += 1'. Example 1 input shows '3,3' — should be [1,2,3,6,2,3,4,7,8]. This walk-back version is actually O(n) amortized, not O(n log n).
> - `greedy_filter_mergetripletstoformtargettriplet` — Code is right. The card labels it LeetCode 1890; it's LC 1899 (Merge Triplets to Form Target Triplet). Example 1 says 'all triplets are valid', but [1,8,4] is invalid (8 > 7) and gets skipped; the answer true is still correct.
> - `greedy_lastindex_partitionlabels` — Code is right. Walkthrough table slips: at i=2 'end (after)' shows 3 but should stay 8, and the last 'e' is at index 15 (not 14), so the second part's end is 15. Final sizes [9,7,8] are correct.
> - `hashing_hashset_validsudoku` — Typo 'contiune' (syntax error). Example 1 board row shows two 2s — drawing error; real row is '. 6 . . . . 2 8 .'.
> - `hashing_normalize_groupshiftedstrings` — The defaultdict import line is garbled — write `from collections import defaultdict`.
> - `linkedlist_hashmap_copylistwithrandompointer` — Bug: visited = {} at class level is shared across calls — initialise it inside the method (or __init__).
> - `linkedlist_reverse_reverselinkedlist` — Step 3 diagram shows 1 → 1 → None; should be 2 → 1 → None.
> - `linkedlist_reverse_reversenodesinkgroup` — Recursive version uses O(n/k) stack, not O(1); iterative version is O(1).
> - `monostack_monotonicdeque_slidingwindowmaximum` — Last frame shows array '1 2 -1…' — should be '1 3 -1…'. Output [3,3,5,5,6,7] is correct.
> - `queue_bfs_nestedlistweightsum2` — Code and example disagree: the correct inverse-depth answer is 8; the card's code (resets level sum each level) returns 9.
> - `recursion_dfs_nestedlistweightsum` — Off by one: starts at depth 1 for the outer list, so top-level integers get weight 2 — they should have weight 1.
> - `slidingwindow_fixed_permutationinstring` — Example 2 diagram boxes are garbled (missing letter); the answer false is still correct.
> - `sorting_mergesort_countinversions` — Card labels it 131 — not a LeetCode problem (LC 131 is Palindrome Partitioning).
> - `stack_indices_validparenthesisstring` — Code is correct but several examples are wrong: Example 2 trace is for '(*))' (input label says '(*)'). Example 3 trace is for '((*))', which is valid (true), not false. 'Invalid case' '(()*' is actually valid (true): after scan left=[0], star=[3], 0<3 matches. 'Valid case' '(*()*' after scan has left=[0], not [0,2] (the ')' at 3 pops 2).
> - `stack_twopass_removeinvalidparentheses` — Titled Remove Invalid Parentheses, but the code solves LC 1249 (Minimum Remove to Make Valid Parentheses).
> - `tree_dfs_binarytreemaximumpathsum` — Card's code re-calls getMax at every node → O(n²) worst case, not O(n). Use one DFS returning max gain and updating a global best.
> - `tree_lca_lowestcommonancestor` — Compares root.val to p/q, but in LC 236 p and q are TreeNodes — compare `root == p or root == q`.
> - `trie_backtracking_wordsearch2_v2` — 'eat' path wrongly starts at (1,0); it is (1,3)e->(1,2)a->(1,1)t. Code typo 'for w inwords'.
> - `twopointers_forwardbackward_minimumwindowsubsequence` — Titled '76' but solves LC 727. For S='abcdebdde', T='bde' the answer is 'bcde' (card shows 'bdde' and 'bde').

> ↪ Duplicate problems (24): the simpler card is kept; these are hidden as alternates in the viewer (toggle *alternates*):
>
> - `backtracking_counting_generateparentheses` → prefer `backtracking_constrained_generateparentheses` — Same open/close backtracking code; this card is clean and correct, the other has a broken walkthrough tree and wrong complexity.
> - `backtracking_dfs_combinationsum` → prefer `backtracking_combinations_combinationsum` — Standard for-loop-from-start backtracking (same template as subsets/combinations), correct and error-free; the include/exclude card has a mislabeled tree node.
> - `backtracking_dfs_wordsearch_v2` → prefer `backtracking_dfs_wordsearch` — Same mark-with-# DFS code; this card's examples are correct, v2's 'SEE' path is wrong.
> - `backtracking_sets_nqueens` → prefer `backtracking_constrained_nqueens` — Same cols/posDiag/negDiag set backtracking; this card is correct, the other mislabels the diagonals.
> - `backtracking_subsets_subsetsii` → prefer `backtracking_dedup_subsets2` — Same sort + skip-same-level backtracking; this card is a bit tighter (no needless nonlocal) and has a correct walkthrough.
> - `design_dll_allo1datastructure` → prefer `design_bucketlist_alloonedatastructure` — Same count-bucket DLL + key->node map, but complete on one card with explicit head/tail sentinels; the prev pair splits concept (inc/dec elided) and code across two cards.
> - `design_dll_allo1datastructure_v2` → prefer `design_bucketlist_alloonedatastructure` — Same count-bucket DLL design; prev v2 is the code half of the two-card prev set (single circular root sentinel), equally valid but the one-card version is easier to revise.
> - `design_ordereddict_lrucache` → prefer `design_hashmapdll_lrucache` — Interviewers usually disallow OrderedDict; hashmap + DLL with dummy head/tail is the expected answer and its code is correct (only the walkthrough list order is off). OrderedDict kept as alt shortcut.
> - `dp_knapsack_coinchange` → prefer `dp_knapsack_coinchange_v2` — Same 1D unbounded-knapsack DP; new card is clearer (examples, trace, memo alt) and the old card's return line is mis-indented
> - `dp_lis_longestincreasingsubsequence_v2` → prefer `dp_lis_longestincreasingsubsequence` — Same LC 300 tails + bisect solution. Existing code is shorter (no special case for empty input, no separate LIS counter); the new card's only extra is the O(n^2) DP baseline.
> - `dp_memo_longestincreasingpathinamatrix_v2` → prefer `dp_memo_longestincreasingpathinamatrix` — Same memoized DFS; existing card is equally short and clean, new card's Example 1 path is wrong
> - `dp_tabulation_houserobber` → prefer `dp_tabulation_houserobber1and2` — Same linear DP; new card adds the O(1) two-variable version (simplest to write) and House Robber II
> - `dp_tabulation_jumpgame2_v2` → prefer `dp_tabulation_jumpgame2` — Same LC 45 right-to-left O(n^2) DP, nearly line for line. Existing uses float('inf') instead of the magic 1000000, so it reads more clearly.
> - `graph_dfs_redundantconnection` → prefer `unionfind_cycledetection_redundantconnection` — Union-find is the standard answer: the first edge whose ends already share a root is the one; the DFS version needs fiddly cycleStart/parent tracking and a reverse edge scan (rank could even be dropped).
> - `graph_multisourcebfs_wallsandgates_v2` → prefer `graph_multisourcebfs_wallsandgates` — Uses the grid itself as the visited marker (only expand into INF, dist = parent + 1), so no visit set or level loop; v2 has an '==' vs '=' bug. Small slip in this card: stray ':' after queue.popleft().
> - `graph_topo_courseschedule2` → prefer `graph_topo_coursescheduleii` — Same Kahn's BFS; this card's code is clean, the other has a 'defaduldict' typo that breaks the import and a dry-run step that puts 3 in the queue too early.
> - `greedy_counting_taskscheduler_v2` → prefer `greedy_counting_taskscheduler` — Same max(len, (f-1)(n+1)+count) formula with clean code and a clear picture; v2 is a standalone card (not a part 2) whose extra heap-sim code has typos (values(!], garbled heappop/popleft).
> - `hashing_normalize_groupshiftedstrings` → prefer `hashing_signature_groupshiftedstrings` — Diff-tuple key is a few lines with no empty-string special case; the normalize card is longer and its defaultdict import is garbled ('defatdiict').
> - `intervals_greedy_nonoverlappingintervals_v2` → prefer `intervals_greedy_nonoverlappingintervals` — Same LC 435 greedy. Existing sorts by end and just counts; the new card sorts by start and needs prevEnd = min(...) on overlap, which is one more thing to get wrong.
> - `tree_lca_lowestcommonancestor` → prefer `tree_lca_lowestcommonancestorofabinarytree` — Same post-order recursion but shorter (one combined base case, 'return left or right'); the other compares root.val to p/q, which are nodes in LC 236.
> - `trie_backtracking_wordsearch2_v2` → prefer `trie_backtracking_wordsearch2` — Storing the word at the trie node and marking cells with '#' means no visited set and no string building, and setting word=None dedupes; v2 has a typo and a wrong 'eat' path.
> - `trie_dfs_designaddandsearchwordsdatastructure_v2` → prefer `trie_dfs_designaddandsearchwordsdatastructure` — Pure recursive dfs(i, node) with one base case is easier to get right than v2's mixed loop-plus-recursion search; both are correct.
> - `twopointers_forwardbackward_minimumwindowsubsequence` → prefer `dp_lastposition_minimumwindowsubsequence` — 1-D dp[j] = start index of s2[0..j] match is one pass, ~12 lines, with no forward/backward pointer-reset trick; both codes are correct, but this card's example answer is wrong (should be 'bcde').
> - `unionfind_dsu_pathwithmaximumminimumvalue` → prefer `graph_dijkstra_pathwithmaximumminimumvalue` — Max-heap Dijkstra is ~20 lines with no DSU class, sort, or active grid, and reuses a familiar template; both are correct (small slip here: stray ':' after len(grid[0])).

## google_coding (main)

231 cards · folder `freeform_google_coding`

| Topic | Count |
|---|---|
| graph | 35 |
| dp | 32 |
| design | 15 |
| intervals | 15 |
| tree | 12 |
| backtracking | 10 |
| heap | 10 |
| trie | 10 |
| greedy | 8 |
| binarysearch | 7 |
| hashing | 7 |
| unionfind | 7 |
| array | 6 |
| linkedlist | 6 |
| slidingwindow | 6 |
| stack | 6 |
| string | 6 |
| twopointers | 6 |
| matrix | 5 |
| prefixsum | 5 |
| sorting | 4 |
| monostack | 3 |
| recursion | 3 |
| bitmanip | 2 |
| bst | 2 |
| concurrency | 1 |
| math | 1 |
| queue | 1 |

### array (6)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [array_boyermoore_majorityelement](coding/freeform_google_coding/array_boyermoore_majorityelement.png) | Majority Element | LC 169 | Boyer-Moore voting with candidate and count, O(n) time O(1) space. |
| [array_boyermoore_majorityelement2](coding/freeform_google_coding/array_boyermoore_majorityelement2.png) | Majority Element II | LC 229 | Two candidates + two counters, then a second pass to verify counts > n/3; O(n) time, O(1) space |
| [array_cyclicsort_firstmissingpositive](coding/freeform_google_coding/array_cyclicsort_firstmissingpositive.png) | First Missing Positive | LC 41 | Place value x at index x-1 by swapping, then scan for first mismatch. |
| [array_reverse_rotatearray](coding/freeform_google_coding/array_reverse_rotatearray.png) | Rotate Array | LC 189 | Rotate right by k via slicing; O(1)-space alternative with three reversals. |
| [array_runlength_adjacentincreasingsubarraysdetection2](coding/freeform_google_coding/array_runlength_adjacentincreasingsubarraysdetection2.png) | Adjacent Increasing Subarrays Detection II | LC 3350 | Track prev/curr increasing run lengths; ans=max(curr//2, min(prev,curr)) at each run end; O(n), O(1) |
| [array_sentinel_missingranges](coding/freeform_google_coding/array_sentinel_missingranges.png) | Missing Ranges | LC 163 | One pass with prev=lower-1 and virtual upper+1 sentinels; emit [prev+1,curr-1] when gap >1; O(n) |

### backtracking (10)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [backtracking_counting_generateparentheses](coding/freeform_google_coding/backtracking_counting_generateparentheses.png) | Generate Parentheses | LC 22 | Backtrack adding '(' while open<n and ')' while close<open; count is the nth Catalan number. |
| [backtracking_dedup_subsets2](coding/freeform_google_coding/backtracking_dedup_subsets2.png) | Subsets II | LC 90 | Sort, add subset at every level, skip nums[j]==nums[j-1] when j>i to avoid duplicate subsets. |
| [backtracking_dfs_combinationsum](coding/freeform_google_coding/backtracking_dfs_combinationsum.png) | Combination Sum | LC 39 | Include/exclude DFS: include nums[i] staying at i (reuse), exclude moves to i+1; prune when total > target. |
| [backtracking_dfs_robotroomcleaner](coding/freeform_google_coding/backtracking_dfs_robotroomcleaner.png) | Robot Room Cleaner | LC 489 | DFS on relative coordinates with visited set; turn right through 4 dirs; physical backtrack (turn 180, move, turn 180); O(R). |
| [backtracking_dfs_wordsearch](coding/freeform_google_coding/backtracking_dfs_wordsearch.png) | Word Search | LC 79 | Grid DFS backtracking from each matching cell, mark visited with '#', restore; O(mn*4^L). |
| [backtracking_dfs_wordsearch_v2](coding/freeform_google_coding/backtracking_dfs_wordsearch_v2.png) | Word Search | LC 79 | DFS from every cell, mark visited with '#', explore 4 neighbors, restore on backtrack; O(R·C·3^L). |
| [backtracking_includeexclude_subsets](coding/freeform_google_coding/backtracking_includeexclude_subsets.png) | Subsets | LC 78 | Binary include/exclude recursion on each index, append copy at i==n; 2^n subsets, O(n·2^n). |
| [backtracking_partition_palindromepartitioning](coding/freeform_google_coding/backtracking_partition_palindromepartitioning.png) | Palindrome Partitioning | LC 131 | Backtrack over cut end-index j, recurse on j+1 when s[i:j+1] is a palindrome (two-pointer check). |
| [backtracking_sets_nqueens](coding/freeform_google_coding/backtracking_sets_nqueens.png) | N-Queens | LC 51 | Row-by-row backtracking with column, r+c and r-c sets to check safety; O(n!). |
| [backtracking_swap_permutations](coding/freeform_google_coding/backtracking_swap_permutations.png) | Permutations | LC 46 | Backtracking by in-place swapping nums[i] with nums[idx], recurse i+1, swap back; O(n·n!). |

### binarysearch (7)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [binarysearch_answer_aggressivecows](coding/freeform_google_coding/binarysearch_answer_aggressivecows.png) | Aggressive Cows |  | Binary search on the minimum gap with a greedy placement feasibility check after sorting stalls. |
| [binarysearch_answer_kokoeatingbananas](coding/freeform_google_coding/binarysearch_answer_kokoeatingbananas.png) | Koko Eating Bananas | LC 875 | Binary search speed k in [1, max(piles)], checking total ceil(p/k) hours <= h. |
| [binarysearch_answer_splitarraylargestsum](coding/freeform_google_coding/binarysearch_answer_splitarraylargestsum.png) | Split Array Largest Sum | LC 410 | Binary search on the answer in [max(a), sum(a)] with a greedy split-count feasibility check. |
| [binarysearch_flatten_searcha2dmatrix](coding/freeform_google_coding/binarysearch_flatten_searcha2dmatrix.png) | Search a 2D Matrix | LC 74 | Treat the matrix as a flattened sorted array and binary search with row=mid//cols, col=mid%cols. |
| [binarysearch_invariant_truefalsetransition](coding/freeform_google_coding/binarysearch_invariant_truefalsetransition.png) | Find a True-to-False Transition |  | Binary search keeping arr[l]=true, arr[r]=false invariant until adjacent; works on unsorted array; O(log n). |
| [binarysearch_partition_medianoftwosortedarrays](coding/freeform_google_coding/binarysearch_partition_medianoftwosortedarrays.png) | Median of Two Sorted Arrays | LC 4 | Binary search a partition on the smaller array so left halves total (m+n+1)//2 and are all <= right halves. |
| [binarysearch_rotated_searchinrotatedsortedarray](coding/freeform_google_coding/binarysearch_rotated_searchinrotatedsortedarray.png) | Search in Rotated Sorted Array | LC 33 | Binary search that detects which half is sorted and checks whether target lies in it. |

### bitmanip (2)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [bitmanip_fulladder_sumoftwointegers](coding/freeform_google_coding/bitmanip_fulladder_sumoftwointegers.png) | Sum of Two Integers | LC 371 | Bit-by-bit full adder over 32 bits with 32-bit mask, convert back via ~(res ^ mask) if sign bit set; O(1) time/space |
| [bitmanip_shift_reversebits](coding/freeform_google_coding/bitmanip_shift_reversebits.png) | Reverse Bits | LC 190 | Loop 32 times: take bit i with (n>>i)&1 and add it at position 31-i; O(1) time and space |

### bst (2)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [bst_bounds_validatebinarysearchtree](coding/freeform_google_coding/bst_bounds_validatebinarysearchtree.png) | Validate Binary Search Tree | LC 98 | DFS passing (low, high) bounds down the tree with strict inequality checks. |
| [bst_lca_lowestcommonancestorofabinarysearchtree](coding/freeform_google_coding/bst_lca_lowestcommonancestorofabinarysearchtree.png) | Lowest Common Ancestor of a Binary Search Tree | LC 235 | Iteratively walk from root using BST ordering until p and q split; O(h) time, O(1) space. |

### concurrency (1)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [concurrency_mutex_trafficlightcontrolledintersection](coding/freeform_google_coding/concurrency_mutex_trafficlightcontrolledintersection.png) | Traffic Light Controlled Intersection | LC 1279 | Single Lock guards green_road state and crossCar; call turnGreen only when switching roads. |

### design (15)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [design_bisect_snapshotarray](coding/freeform_google_coding/design_bisect_snapshotarray.png) | Snapshot Array | LC 1146 | Per-index history of (snap_id, value); bisect_right for get, overwrite on repeated set in same snap. |
| [design_bisect_timebasedkeyvaluestore](coding/freeform_google_coding/design_bisect_timebasedkeyvaluestore.png) | Time Based Key-Value Store | LC 981 | Hashmap key -> sorted (timestamp, value) list; binary search for rightmost timestamp <= target. |
| [design_bucket_loosemediandatastructure](coding/freeform_google_coding/design_bucket_loosemediandatastructure.png) | Loose Median Data Structure |  | 64 power-of-2 buckets keyed by bit_length; scan cumulative counts to find median bucket, return 2^k. |
| [design_bucketlist_alloonedatastructure](coding/freeform_google_coding/design_bucketlist_alloonedatastructure.png) | All O(1) Data Structure | LC 432 | Hash Map + Doubly Linked List of Count Buckets |
| [design_hashmap_loggerratelimiter](coding/freeform_google_coding/design_hashmap_loggerratelimiter.png) | Logger Rate Limiter | LC 359 | Hash map message -> next allowed timestamp; print if timestamp >= next_allowed, set to t+10. |
| [design_hashmaparray_insertdeletegetrandomo1](coding/freeform_google_coding/design_hashmaparray_insertdeletegetrandomo1.png) | Insert Delete GetRandom O(1) | LC 380 | Array + value->index hashmap; remove by swapping with last and popping; getRandom via random.choice. |
| [design_hashmapdll_lrucache](coding/freeform_google_coding/design_hashmapdll_lrucache.png) | LRU Cache | LC 146 | Hash map + doubly linked list with dummy head/tail for O(1) get/put and LRU eviction. |
| [design_iterator_rleiterator](coding/freeform_google_coding/design_iterator_rleiterator.png) | RLE Iterator | LC 900 | Pointer over (count,value) pairs; next(n) consumes runs, decrementing counts in place; O(runs) total |
| [design_lazyheap_stockpricefluctuation](coding/freeform_google_coding/design_lazyheap_stockpricefluctuation.png) | Stock Price Fluctuation | LC 2034 | Hashmap timestamp->price plus min/max heaps with lazy deletion of stale entries. |
| [design_lazypropagation_stackwithincrementoperation](coding/freeform_google_coding/design_lazypropagation_stackwithincrementoperation.png) | Design a Stack With Increment Operation | LC 1381 | Parallel lazy inc array; increment marks inc[min(k,size)-1], pop applies and propagates down; all ops O(1) |
| [design_ordereddict_lfucache](coding/freeform_google_coding/design_ordereddict_lfucache.png) | LFU Cache | LC 460 | O(1) LFU via key->(val,freq), freq->OrderedDict buckets and min_freq; LRU tie-break on eviction. |
| [design_quickselect_filesystemsizeanalysis](coding/freeform_google_coding/design_quickselect_filesystemsizeanalysis.png) | File System Size Analysis |  | Trie of paths with total/immediate sizes via DFS; getSize plus k largest files/folders via quickselect. |
| [design_slidingwindow_designaratelimiter](coding/freeform_google_coding/design_slidingwindow_designaratelimiter.png) | Design a Rate Limiter |  | Thread-safe sliding-window limiter: deque of timestamps in last 1000 ms guarded by a Lock. |
| [design_trie_designinmemoryfilesystem](coding/freeform_google_coding/design_trie_designinmemoryfilesystem.png) | Design In-Memory File System | LC 588 | Trie of path components (FileNode with children/is_file/content) supporting mkdir, ls, add/read file. |
| [design_twostacks_designatexteditor](coding/freeform_google_coding/design_twostacks_designatexteditor.png) | Design a Text Editor | LC 2296 | Text editor with cursor using left/right stacks; add, delete, move cursor returning last 10 chars. |

### dp (32)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [dp_hashmap_targetsum](coding/freeform_google_coding/dp_hashmap_targetsum.png) | Target Sum | LC 494 | Layer-by-layer DP over a hashmap of reachable sums -> ways (add and subtract each num), O(S) space variant; O(n*S) time |
| [dp_interval_burstballoons](coding/freeform_google_coding/dp_interval_burstballoons.png) | Burst Balloons | LC 312 | Interval DP, pad with 1s, pick i as LAST balloon in [l,r]: dp[l][r]=max(new[l-1]*new[i]*new[r+1]+dp[l][i-1]+dp[i+1][r]); O(n^3) time, O(n^2) space |
| [dp_interval_longestpalindromicsubstring](coding/freeform_google_coding/dp_interval_longestpalindromicsubstring.png) | Longest Palindromic Substring | LC 5 | dp[i][j] palindrome table: s[i]==s[j] and (len 2 or dp[i+1][j-1]); O(n^2). |
| [dp_kadane_maximumproductsubarray](coding/freeform_google_coding/dp_kadane_maximumproductsubarray.png) | Maximum Product Subarray | LC 152 | Kadane variant tracking current max and min product, swapping them on negative numbers. |
| [dp_kadane_maximumsubarray](coding/freeform_google_coding/dp_kadane_maximumsubarray.png) | Maximum Subarray | LC 53 | dp[i] = max(nums[i], dp[i-1]+nums[i]); Kadane's O(1)-space version. |
| [dp_knapsack_01knapsackbinaryprofit](coding/freeform_google_coding/dp_knapsack_01knapsackbinaryprofit.png) | 0/1 Knapsack (Binary Profit) |  | Standard 1D 0/1 knapsack with reverse capacity iteration, profits restricted to 1 or 2; O(n*capacity). |
| [dp_knapsack_coinchange2](coding/freeform_google_coding/dp_knapsack_coinchange2.png) | Coin Change II | LC 518 | Unbounded knapsack counting: dp[i][a]=dp[i+1][a]+dp[i][a-coin]; 1D version loops coins outer, amount inner ascending (dp[a]+=dp[a-coin]); O(n*amount) time, O(amount) space |
| [dp_knapsack_coinchange_v2](coding/freeform_google_coding/dp_knapsack_coinchange_v2.png) | Coin Change | LC 322 | Unbounded-knapsack bottom-up dp[a]=min(1+dp[a-c]) with amount+1 as infinity, plus top-down lru_cache version; O(amount*n) time, O(amount) space |
| [dp_knapsack_partitionequalsubsetsum](coding/freeform_google_coding/dp_knapsack_partitionequalsubsetsum.png) | Partition Equal Subset Sum | LC 416 | 0/1 subset-sum DP to target=sum/2, 2D table plus 1D backwards version; O(n*target) time, O(target) space |
| [dp_lis_longestincreasingsubsequence](coding/freeform_google_coding/dp_lis_longestincreasingsubsequence.png) | Longest Increasing Subsequence | LC 300 | Patience sorting tails array + bisect_left, O(n log n); O(n^2) DP alternative |
| [dp_lis_longestincreasingsubsequence_v2](coding/freeform_google_coding/dp_lis_longestincreasingsubsequence_v2.png) | Longest Increasing Subsequence (LIS) | LC 300 | Patience sorting tails + bisect_left O(n log n), plus O(n^2) DP LIS[i]=1+max LIS[j] for j>i with nums[j]>nums[i]; O(n) space |
| [dp_memo_lastkeptballblueprobability](coding/freeform_google_coding/dp_memo_lastkeptballblueprobability.png) | Last Kept Ball Is Blue |  | Probability DP with state (red, blue, prev_blue); second consecutive blue is kept, first returned; answer 17/24. |
| [dp_memo_longestincreasingpathinamatrix](coding/freeform_google_coding/dp_memo_longestincreasingpathinamatrix.png) | Longest Increasing Path in a Matrix | LC 329 | Memoized DFS from every cell to strictly larger neighbors (DAG, no cycles); O(m*n) |
| [dp_memo_longestincreasingpathinamatrix_v2](coding/freeform_google_coding/dp_memo_longestincreasingpathinamatrix_v2.png) | Longest Increasing Path in a Matrix | LC 329 | Memoized DFS from every cell passing prevVal, recurse only into strictly larger neighbors, answer = max memo value; O(m*n) time and space |
| [dp_minimax_stonegame3](coding/freeform_google_coding/dp_minimax_stonegame3.png) | Stone Game III | LC 1406 | Minimax DP on score difference, taking 1-3 stones; sign of dp[0] decides winner. |
| [dp_prefixsum_numberofzigzagarrays1](coding/freeform_google_coding/dp_prefixsum_numberofzigzagarrays1.png) | Number of ZigZag Arrays I | LC 3699 | up[j]/down[j] DP by last direction, transitions via prefix/suffix sums for O(n*k). |
| [dp_segmenttree_longestincreasingsubsequenceii](coding/freeform_google_coding/dp_segmenttree_longestincreasingsubsequenceii.png) | Longest Increasing Subsequence II | LC 2407 | dp[x] = 1 + max dp over values [x-k, x-1] via segment tree range-max query + point update; O(N log M). |
| [dp_statemachine_besttimetobuyandsellstockwithcooldown](coding/freeform_google_coding/dp_statemachine_besttimetobuyandsellstockwithcooldown.png) | Best Time to Buy and Sell Stock with Cooldown | LC 309 | State DP from right to left: dp[i][buy]=max(-p+dp[i+1][hold], dp[i+1][buy]); dp[i][hold]=max(p+dp[i+2][buy], dp[i+1][hold]); O(n) time, O(1) with 3 vars |
| [dp_tabulation_decodeways](coding/freeform_google_coding/dp_tabulation_decodeways.png) | Decode Ways | LC 91 | Right-to-left DP: dp[i]=dp[i+1] if s[i]!='0', plus dp[i+2] if s[i:i+2] is 10-26; O(n) time, O(n) or O(1) with two variables |
| [dp_tabulation_distinctsubsequences](coding/freeform_google_coding/dp_tabulation_distinctsubsequences.png) | Distinct Subsequences | LC 115 | 2D DP dp[i][j]=ways to form t[j:] from s[i:]: skip s[i] + (match ? dp[i+1][j+1]); dp[i][n]=1; O(mn) time/space, O(n) with 1D |
| [dp_tabulation_dungeongame](coding/freeform_google_coding/dp_tabulation_dungeongame.png) | Dungeon Game | LC 174 | Reverse bottom-up DP for min initial health: dp[i][j]=max(1, min(right,down)-cell). |
| [dp_tabulation_editdistance](coding/freeform_google_coding/dp_tabulation_editdistance.png) | Edit Distance | LC 72 | Suffix 2D DP: match -> dp[i+1][j+1], else 1+min(delete, insert, replace); bases dp[m][j]=n-j, dp[i][n]=m-i; O(mn) time/space, O(n) rolling |
| [dp_tabulation_houserobber1and2](coding/freeform_google_coding/dp_tabulation_houserobber1and2.png) | House Robber / House Robber II | LC 198 / LC 213 | dp[i]=max(dp[i-1], nums[i]+dp[i-2]) with an O(1) two-variable version; II runs it twice on nums[1:] and nums[:-1]; O(n) time |
| [dp_tabulation_interleavingstring](coding/freeform_google_coding/dp_tabulation_interleavingstring.png) | Interleaving String | LC 97 | Suffix 2D DP dp[i][j]=(s1[i]==s3[i+j] and dp[i+1][j]) or (s2[j]==s3[i+j] and dp[i][j+1]), dp[m][n]=True, length check first; O(mn) time, O(n) possible |
| [dp_tabulation_jumpgame2](coding/freeform_google_coding/dp_tabulation_jumpgame2.png) | Jump Game II | LC 45 | Right-to-left O(n^2) DP of min jumps to last index (notes greedy O(n) alternative). |
| [dp_tabulation_jumpgame2_v2](coding/freeform_google_coding/dp_tabulation_jumpgame2_v2.png) | Jump Game II | LC 45 | Right-to-left DP dp[i]=1+min dp[j] for j in (i, i+nums[i]], dp[n-1]=0; O(n^2) time, O(n) space (greedy O(n) mentioned) |
| [dp_tabulation_longestcommonsubsequence](coding/freeform_google_coding/dp_tabulation_longestcommonsubsequence.png) | Longest Common Subsequence | LC 1143 | Suffix DP: match -> 1+dp[i+1][j+1], else max(dp[i+1][j], dp[i][j+1]), plus rolling 1D row; O(m*n) time, O(n) space |
| [dp_tabulation_mincostclimbingstairs](coding/freeform_google_coding/dp_tabulation_mincostclimbingstairs.png) | Min Cost Climbing Stairs | LC 746 | dp[i]=min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2]), dp[0]=dp[1]=0, answer dp[n]; O(n) time, O(1) with two vars |
| [dp_tabulation_minimumtimetofinishtherace](coding/freeform_google_coding/dp_tabulation_minimumtimetofinishtherace.png) | Minimum Time to Finish the Race | LC 2188 | Precompute best[k] for k consecutive laps per tire, then dp[i] = min(dp[i-k] + changeTime + best[k]). |
| [dp_tabulation_regularexpressionmatching](coding/freeform_google_coding/dp_tabulation_regularexpressionmatching.png) | Regular Expression Matching | LC 10 | 2D DP over s/p with '.' and '*' transitions (zero vs one-or-more occurrences), worked table. |
| [dp_tabulation_uniquepaths](coding/freeform_google_coding/dp_tabulation_uniquepaths.png) | Unique Paths | LC 62 | Grid DP from bottom-right: dp[i][j]=dp[i+1][j]+dp[i][j+1], 1D row version, plus C(m+n-2, m-1) formula; O(m*n) time, O(n) space |
| [dp_tabulation_wordbreak](coding/freeform_google_coding/dp_tabulation_wordbreak.png) | Word Break | LC 139 | Boolean dp[j] = exists i<j with dp[i] and s[i:j] in word set; optional max_len pruning; O(n^2). |

### graph (35)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [graph_bellmanford_cheapestflightswithinkstops](coding/freeform_google_coding/graph_bellmanford_cheapestflightswithinkstops.png) | Cheapest Flights Within K Stops | LC 787 | Bounded Bellman-Ford: k+1 relaxation rounds using a temp copy of dist each round; O((k+1)E). |
| [graph_bfs_busroutes](coding/freeform_google_coding/graph_bfs_busroutes.png) | Bus Routes | LC 815 | BFS over stops with stop->buses map and visited_buses to avoid re-expanding routes. |
| [graph_bfs_escapethespreadingfire](coding/freeform_google_coding/graph_bfs_escapethespreadingfire.png) | Escape the Spreading Fire | LC 2258 | Multi-source BFS for fire arrival times, then binary search on wait time with BFS feasibility check (safehouse allows tie). |
| [graph_bfs_graphvalidtree](coding/freeform_google_coding/graph_bfs_graphvalidtree.png) | Graph Valid Tree | LC 261 | Reject if edges > n-1, BFS with parent to detect cycles, then require all n nodes visited. |
| [graph_bfs_minimumknightmoves](coding/freeform_google_coding/graph_bfs_minimumknightmoves.png) | Minimum Knight Moves | LC 1197 | BFS over 8 knight moves using abs(x), abs(y) symmetry and a small negative buffer (>= -2); visited set. |
| [graph_bfs_minimummovestomoveabox](coding/freeform_google_coding/graph_bfs_minimummovestomoveabox.png) | Minimum Moves to Move a Box to Their Target Location | LC 1263 | Outer BFS over (box, player) states where each step is a push; inner BFS checks player can reach the cell behind the box. |
| [graph_bfs_routermessagereachability](coding/freeform_google_coding/graph_bfs_routermessagereachability.png) | Router Message Reachability |  | Implicit graph of routers connected within wireless range (squared distance); BFS from source to target; O(n^2). |
| [graph_dfs_clonegraph](coding/freeform_google_coding/graph_dfs_clonegraph.png) | Clone Graph | LC 133 | DFS with hashmap original->clone, store clone before recursing on neighbors to handle cycles; O(V+E). |
| [graph_dfs_countlakesin2dgrid](coding/freeform_google_coding/graph_dfs_countlakesin2dgrid.png) | Count Lakes in a 2D Grid |  | Connected components of water cells via DFS or BFS with visited set; O(mn). |
| [graph_dfs_countsubislands](coding/freeform_google_coding/graph_dfs_countsubislands.png) | Count Sub Islands | LC 1905 | DFS each grid2 island, checking every cell is land in grid1; explore fully before counting. |
| [graph_dfs_evaluatedivision](coding/freeform_google_coding/graph_dfs_evaluatedivision.png) | Evaluate Division | LC 399 | Weighted bidirectional graph (k and 1/k); DFS path product answers each query, -1.0 if none. |
| [graph_dfs_floodfill](coding/freeform_google_coding/graph_dfs_floodfill.png) | Flood Fill | LC 733 | 4-directional DFS recolor of cells matching original color; return early if color already equal. |
| [graph_dfs_maxareaofisland](coding/freeform_google_coding/graph_dfs_maxareaofisland.png) | Max Area of Island | LC 695 | Recursive DFS returning 1 + sum of 4 neighbors with a visited set; track max over all land cells. |
| [graph_dfs_numberofclosedislands](coding/freeform_google_coding/graph_dfs_numberofclosedislands.png) | Number of Closed Islands | LC 1254 | Flood-fill boundary-connected land with DFS, then count remaining 0-islands in the interior. |
| [graph_dfs_numberofprovinces](coding/freeform_google_coding/graph_dfs_numberofprovinces.png) | Number of Provinces | LC 547 | Count connected components in adjacency matrix: DFS from each unvisited city increments count; O(n^2). |
| [graph_dfs_pacificatlanticwaterflow](coding/freeform_google_coding/graph_dfs_pacificatlanticwaterflow.png) | Pacific Atlantic Water Flow | LC 417 | Reverse multi-source DFS from each ocean's borders climbing to >= heights; answer is intersection. |
| [graph_dfs_redundantconnection](coding/freeform_google_coding/graph_dfs_redundantconnection.png) | Redundant Connection | LC 684 | DFS with parent tracking to collect cycle nodes, then return last edge (reverse scan) with both endpoints in the cycle. |
| [graph_dfs_surroundedregions](coding/freeform_google_coding/graph_dfs_surroundedregions.png) | Surrounded Regions | LC 130 | DFS from border 'O's marking them 'T', then flip remaining 'O' to 'X' and restore 'T' to 'O'. |
| [graph_dijkstra_findthesafestpathinagrid](coding/freeform_google_coding/graph_dijkstra_findthesafestpathinagrid.png) | Find the Safest Path in a Grid | LC 2812 | Multi-source BFS distance to thieves, then max-heap Dijkstra maximizing min safeness. |
| [graph_dijkstra_minimumsecurityclearance](coding/freeform_google_coding/graph_dijkstra_minimumsecurityclearance.png) | Minimum Security Clearance |  | Minimax Dijkstra (ns = max(sec, edge_sec)); variant with lexicographic (security, cost) tuples in heap. |
| [graph_dijkstra_networkdelaytime](coding/freeform_google_coding/graph_dijkstra_networkdelaytime.png) | Network Delay Time | LC 743 | Dijkstra with min-heap from k; answer is max shortest distance, -1 if any node unreachable; O((V+E) log V). |
| [graph_dijkstra_pathwithmaximumminimumvalue](coding/freeform_google_coding/graph_dijkstra_pathwithmaximumminimumvalue.png) | Path With Maximum Minimum Value | LC 1102 | Max-heap Dijkstra maximizing bottleneck: new_score = min(score, cell); first pop of destination is answer. |
| [graph_dijkstra_swiminrisingwater](coding/freeform_google_coding/graph_dijkstra_swiminrisingwater.png) | Swim in Rising Water | LC 778 | Minimax Dijkstra: min-heap keyed by max elevation on path so far, return when bottom-right is popped; O(n^2 log n) time, O(n^2) space |
| [graph_dijkstra_themaze2](coding/freeform_google_coding/graph_dijkstra_themaze2.png) | The Maze II | LC 505 | Dijkstra over stopping positions; roll each direction until wall, edge weight = steps; O(mn(m+n) log mn) |
| [graph_hierholzer_reconstructitinerary](coding/freeform_google_coding/graph_hierholzer_reconstructitinerary.png) | Reconstruct Itinerary | LC 332 | Eulerian path via Hierholzer's: min-heap adjacency for lexical order, postorder append, reverse; O(E log E) |
| [graph_multisourcebfs_rottingoranges](coding/freeform_google_coding/graph_multisourcebfs_rottingoranges.png) | Rotting Oranges | LC 994 | Multi-source BFS from all rotten cells, level = minute, track fresh count; -1 if any remain; O(mn) |
| [graph_multisourcebfs_wallsandgates](coding/freeform_google_coding/graph_multisourcebfs_wallsandgates.png) | Walls and Gates | LC 286 | Multi-source BFS from all 0 cells, fill INF land cells with dist+1 in place; O(mn). |
| [graph_multisourcebfs_wallsandgates_v2](coding/freeform_google_coding/graph_multisourcebfs_wallsandgates_v2.png) | Walls and Gates | LC 286 | Multi-source BFS from all gates level by level, writing distance into empty rooms. |
| [graph_prim_mincosttoconnectallpoints](coding/freeform_google_coding/graph_prim_mincosttoconnectallpoints.png) | Min Cost to Connect All Points | LC 1584 | MST on complete Manhattan-distance graph via dense O(n^2) Prim's with min_dist array. |
| [graph_retrogradebfs_catandmouse](coding/freeform_google_coding/graph_retrogradebfs_catandmouse.png) | Cat and Mouse | LC 913 | Game theory over (mouse, cat, turn) states; reverse BFS from terminal states with degree counting. |
| [graph_topo_aliendictionary](coding/freeform_google_coding/graph_topo_aliendictionary.png) | Alien Dictionary | LC 269 | Edges from first differing char of adjacent words, Kahn's topo sort; invalid prefix or cycle returns empty. |
| [graph_topo_buildamatrixwithconditions](coding/freeform_google_coding/graph_topo_buildamatrixwithconditions.png) | Build a Matrix With Conditions | LC 2392 | Two independent Kahn topo sorts (row and column constraints); cycle -> []; place x at (rowPos[x], colPos[x]). |
| [graph_topo_courseschedule](coding/freeform_google_coding/graph_topo_courseschedule.png) | Course Schedule | LC 207 | Kahn's BFS topological sort with indegrees; possible iff all courses get processed. |
| [graph_topo_coursescheduleii](coding/freeform_google_coding/graph_topo_coursescheduleii.png) | Course Schedule II | LC 210 | Kahn's BFS topological sort with indegrees to return a valid course order; empty if cycle. |
| [graph_topo_sequencereconstruction](coding/freeform_google_coding/graph_topo_sequencereconstruction.png) | Sequence Reconstruction | LC 444 | Kahn's topo sort over adjacent-pair edges; unique iff queue size is always 1 and order equals nums. |

### greedy (8)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [greedy_counting_handofstraights](coding/freeform_google_coding/greedy_counting_handofstraights.png) | Hand of Straights | LC 846 | Counter + walk back to smallest start of each consecutive run, greedily peel groups of size k; O(n) amortized (card says O(n log n)), O(n) space |
| [greedy_counting_taskscheduler](coding/freeform_google_coding/greedy_counting_taskscheduler.png) | Task Scheduler | LC 621 | Formula max(len(tasks), (f-1)*(n+1)+k) using max frequency f and count k of most frequent tasks. |
| [greedy_counting_taskscheduler_v2](coding/freeform_google_coding/greedy_counting_taskscheduler_v2.png) | Task Scheduler | LC 621 | Counting formula max(len(tasks), (f-1)*(n+1)+count) plus max-heap + cooldown-queue simulation alternative. |
| [greedy_differencearray_minimumnumberofincrementsonsubarraystoformatargetarray](coding/freeform_google_coding/greedy_differencearray_minimumnumberofincrementsonsubarraystoformatargetarray.png) | Minimum Number of Increments on Subarrays to Form a Target Array | LC 1526 | Answer = target[0] + sum of positive adjacent differences (histogram layers view). |
| [greedy_filter_mergetripletstoformtargettriplet](coding/freeform_google_coding/greedy_filter_mergetripletstoformtargettriplet.png) | Merge Triplets | LC 1899 | Skip any triplet exceeding target in some slot; among the rest, record which positions hit target exactly; true if all 3 hit; O(n) time, O(1) space |
| [greedy_lastindex_partitionlabels](coding/freeform_google_coding/greedy_lastindex_partitionlabels.png) | Partition Labels | LC 763 | Record last index of each char; scan extending end=max(end,last[c]) and cut when i==end; O(n) time, O(1) space |
| [greedy_linefill_numberoflinestowritestring](coding/freeform_google_coding/greedy_linefill_numberoflinestowritestring.png) | Number of Lines To Write String | LC 806 | Greedily fill 100px lines with per-letter widths, new line on overflow; return [lines, last width]; O(n) |
| [greedy_runningsum_gasstation](coding/freeform_google_coding/greedy_runningsum_gasstation.png) | Gas Station | LC 134 | If sum(gas)<sum(cost) return -1; else one pass with running tank, reset tank and set start=i+1 whenever it goes negative; O(n) time, O(1) space |

### hashing (7)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [hashing_counting_findoriginalarrayfromdoubledarray](coding/freeform_google_coding/hashing_counting_findoriginalarrayfromdoubledarray.png) | Find Original Array From Doubled Array | LC 2007 | Sort + Counter greedy pairing of x with 2x, handling zeros and odd length. |
| [hashing_counting_senderwithlargestwordcount](coding/freeform_google_coding/hashing_counting_senderwithlargestwordcount.png) | Sender With Largest Word Count | LC 2284 | Hashmap sender->word count via split; pick max with lexicographically-largest tie-break; O(T) |
| [hashing_groupby_friendrecommendations](coding/freeform_google_coding/hashing_groupby_friendrecommendations.png) | Friend Recommendations |  | Dedupe listens, group users by (day, song), count shared songs per user pair/day, keep >=3 and exclude existing friends. |
| [hashing_hashset_longestconsecutivesequence](coding/freeform_google_coding/hashing_hashset_longestconsecutivesequence.png) | Longest Consecutive Sequence | LC 128 | Hash set, start counting only at sequence starts (n-1 not in set), O(n). |
| [hashing_hashset_validsudoku](coding/freeform_google_coding/hashing_hashset_validsudoku.png) | Valid Sudoku | LC 36 | Hash sets per row, column and 3x3 box (keyed r//3, c//3) to detect duplicate digits. |
| [hashing_normalize_groupshiftedstrings](coding/freeform_google_coding/hashing_normalize_groupshiftedstrings.png) | Group Shifted Strings | LC 249 | Normalize each string so first char is 'a' (mod 26) and group by that key; alt diff-tuple key. |
| [hashing_remapping_randompickwithblacklist](coding/freeform_google_coding/hashing_remapping_randompickwithblacklist.png) | Random Pick with Blacklist | LC 710 | Sample from [0, M-1] (M = n - |

### heap (10)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [heap_greedymatching_processorderspartialfulfillment](coding/freeform_google_coding/heap_greedymatching_processorderspartialfulfillment.png) | Process Orders with Partial Fulfillment |  | Min-heap of Fizz supply by cost; each Buzz pops cheapest, partial match, push back remainder; O((n+k) log n) |
| [heap_kway_mergeksortedlists](coding/freeform_google_coding/heap_kway_mergeksortedlists.png) | Merge K Sorted Lists | LC 23 | K-way merge pushing (val, list_idx, node) into a min-heap; O(N log k). |
| [heap_sweepline_skylineproblem](coding/freeform_google_coding/heap_sweepline_skylineproblem.png) | The Skyline Problem | LC 218 | Start/end events sorted by x, sweep with lazy-deletion max-heap of (-h,right); emit key point on max change; O(N log N) |
| [heap_topk_findtop5largestfilesindirectorytree](coding/freeform_google_coding/heap_topk_findtop5largestfilesindirectorytree.png) | Top 5 Largest Files in a Directory Tree |  | DFS the directory tree via list_dir/size_of, keep a size-5 min-heap of (size, path), return sorted desc. |
| [heap_topk_movierecommendationsystem](coding/freeform_google_coding/heap_topk_movierecommendationsystem.png) | Movie Recommendation System |  | Weighted content similarity (genres, cast, director, rating diff) + size-K min-heap with id tie-break; O(N log K) |
| [heap_topk_topkchatcontributors](coding/freeform_google_coding/heap_topk_topkchatcontributors.png) | Top K Chat Contributors |  | Counter + size-k min-heap, pop for ascending (reverse) order; nlargest alternative; O(N + U log k) |
| [heap_topk_topkfrequentelements](coding/freeform_google_coding/heap_topk_topkfrequentelements.png) | Top K Frequent Elements | LC 347 | Count frequencies, keep a size-k min-heap of (freq, num); O(n log k), bucket sort alternative. |
| [heap_twoheaps_findmedianfromdatastream](coding/freeform_google_coding/heap_twoheaps_findmedianfromdatastream.png) | Find Median from Data Stream | LC 295 | Max-heap lower half + min-heap upper half, rebalance on add; median from heap tops. |
| [heap_twoheaps_meetingrooms3](coding/freeform_google_coding/heap_twoheaps_meetingrooms3.png) | Meeting Rooms III | LC 2402 | Sort by start; available-rooms heap + busy (end,room) heap, delay meetings when none free; count per room; O(m log m + m log n) |
| [heap_twoheaps_slidingwindowmedian](coding/freeform_google_coding/heap_twoheaps_slidingwindowmedian.png) | Sliding Window Median | LC 480 | Two heaps with lazy deletion hashmap and size balancing to report median of each size-k window. |

### intervals (15)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [intervals_greedy_minimumnumberofarrowstoburstballoons](coding/freeform_google_coding/intervals_greedy_minimumnumberofarrowstoburstballoons.png) | Minimum Number of Arrows to Burst Balloons | LC 452 | Sort by end, shoot at earliest end, reuse arrow while start <= arrow_pos; new arrow otherwise. |
| [intervals_greedy_nonoverlappingintervals](coding/freeform_google_coding/intervals_greedy_nonoverlappingintervals.png) | Non-overlapping Intervals | LC 435 | Sort by end, greedily keep if start >= prev_end, count removals; O(n log n) |
| [intervals_greedy_nonoverlappingintervals_v2](coding/freeform_google_coding/intervals_greedy_nonoverlappingintervals_v2.png) | Erase Overlap Intervals | LC 435 | Sort by start; on overlap count a removal and keep the smaller end (prevEnd=min); O(n log n) time, O(1) space |
| [intervals_merge_employeefreetime](coding/freeform_google_coding/intervals_merge_employeefreetime.png) | Employee Free Time | LC 759 | Flatten all schedules, sort by start, merge busy intervals, output gaps as common free time; O(N log N). |
| [intervals_merge_finduncoveredrangesinarray](coding/freeform_google_coding/intervals_merge_finduncoveredrangesinarray.png) | Find Uncovered Ranges |  | Sort ranges by start, track first uncovered position, emit gaps before each range and a final tail gap. |
| [intervals_merge_insertinterval](coding/freeform_google_coding/intervals_merge_insertinterval.png) | Insert Interval | LC 57 | Three-phase linear scan: add intervals before, merge overlapping into newInterval, add rest; O(n) |
| [intervals_minheap_assigncarstorentalrequests](coding/freeform_google_coding/intervals_minheap_assigncarstorentalrequests.png) | Assign Cars to Rental Requests |  | Sort by pickup; busy heap of (return, car_id) and available heap of free ids; reuse lowest free car, else new id. |
| [intervals_minheap_meetingroomsii](coding/freeform_google_coding/intervals_minheap_meetingroomsii.png) | Meeting Rooms II | LC 253 | Sort by start, min-heap of end times (reuse room if start >= heap[0]); alt sweep line with sorted starts/ends; O(n log n). |
| [intervals_overlap_mycalendar1](coding/freeform_google_coding/intervals_overlap_mycalendar1.png) | My Calendar I | LC 729 | List of bookings; reject if s1<e2 and e1>s2 (half-open, touching allowed); O(n) per book |
| [intervals_overlap_mycalendar2](coding/freeform_google_coding/intervals_overlap_mycalendar2.png) | My Calendar II | LC 731 | Keep bookings and double-booked overlaps lists; reject if new event hits an overlap, else add intersections; O(n) per book |
| [intervals_segmenttree_rangemodule](coding/freeform_google_coding/intervals_segmenttree_rangemodule.png) | Range Module | LC 715 | Add/query/remove half-open ranges via sorted disjoint interval list, or dynamic segment tree with lazy propagation. |
| [intervals_sweepline_minimumintervaltoincludeeachquery](coding/freeform_google_coding/intervals_sweepline_minimumintervaltoincludeeachquery.png) | Minimum Interval to Include Each Query | LC 1851 | Sort intervals and queries; sweep with min-heap of (size,right), pop expired; O((N+Q) log N) |
| [intervals_sweepline_mycalendar3](coding/freeform_google_coding/intervals_sweepline_mycalendar3.png) | My Calendar III | LC 732 | Difference map +1/-1 at start/end, prefix-sum over sorted times for max active k; O(n log n) per booking |
| [intervals_sweepline_separatesquaresii_card1](coding/freeform_google_coding/intervals_sweepline_separatesquaresii_card1.png) | Separate Squares II (Algorithm) | LC 3454 | Sweep y-events with coordinate-compressed segment tree for union x-length; find y where area below = total/2. |
| [intervals_sweepline_separatesquaresii_card2](coding/freeform_google_coding/intervals_sweepline_separatesquaresii_card2.png) | Separate Squares II (Explanation) | LC 3454 | Sweep line over y-events with coordinate-compressed segment tree tracking covered x-length; find y where union area splits in half; O(n log n). |

### linkedlist (6)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [linkedlist_fastslow_findtheduplicatenumber](coding/freeform_google_coding/linkedlist_fastslow_findtheduplicatenumber.png) | Find the Duplicate Number | LC 287 | Treat index->nums[index] as linked list; Floyd meeting point then cycle entrance. |
| [linkedlist_fastslow_reorderlist](coding/freeform_google_coding/linkedlist_fastslow_reorderlist.png) | Reorder List | LC 143 | Find middle with slow/fast, reverse second half, then merge the two halves alternately in place. |
| [linkedlist_hashmap_copylistwithrandompointer](coding/freeform_google_coding/linkedlist_hashmap_copylistwithrandompointer.png) | Copy List with Random Pointer | LC 138 | Recursive deep copy using an original-to-copy hash map to reuse nodes and handle cycles. |
| [linkedlist_mergesort_sortlist](coding/freeform_google_coding/linkedlist_mergesort_sortlist.png) | Sort List | LC 148 | Merge sort on linked list: fast/slow split (fast=head.next), recurse, merge with dummy node. |
| [linkedlist_reverse_reverselinkedlist](coding/freeform_google_coding/linkedlist_reverse_reverselinkedlist.png) | Reverse Linked List | LC 206 | Iterative prev/curr/temp pointer reversal with step-by-step walkthrough. |
| [linkedlist_reverse_reversenodesinkgroup](coding/freeform_google_coding/linkedlist_reverse_reversenodesinkgroup.png) | Reverse Nodes in k-Group | LC 25 | Count k nodes ahead, reverse exactly k with a helper, recurse on the rest and link the old head to it. |

### math (1)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [math_fastpow_powxn](coding/freeform_google_coding/math_fastpow_powxn.png) | Pow(x, n) | LC 50 | Binary exponentiation by squaring, handling negative exponent via 1/x. |

### matrix (5)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [matrix_boundary_spiralmatrixandaddtwonumbers](coding/freeform_google_coding/matrix_boundary_spiralmatrixandaddtwonumbers.png) | Spiral Matrix and Add Two Numbers | LC 54 / LC 2 | Two-problem card: four-boundary spiral traversal, and linked-list digit addition with carry. |
| [matrix_markers_setmatrixzeroes](coding/freeform_google_coding/matrix_markers_setmatrixzeroes.png) | Set Matrix Zeroes | LC 73 | Use first row/column as zero markers plus a zeroInFirstCol flag, then fill bottom-right to top-left; O(mn) time, O(1) space |
| [matrix_simulation_spiralmatrix](coding/freeform_google_coding/matrix_simulation_spiralmatrix.png) | Spiral Matrix | LC 54 | Four shrinking boundaries, traverse top/right/bottom/left with up!=down and left!=right guards. |
| [matrix_slotscan_checkifwordcanbeplacedincrossword](coding/freeform_google_coding/matrix_slotscan_checkifwordcanbeplacedincrossword.png) | Check if Word Can Be Placed In Crossword | LC 2018 | Scan maximal #-bounded row/column slots; match exact length against word or its reverse; O(m*n) |
| [matrix_transpose_rotateimage](coding/freeform_google_coding/matrix_transpose_rotateimage.png) | Rotate Image | LC 48 | Transpose across the main diagonal, then reverse each row; O(n^2) time, O(1) space |

### monostack (3)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [monostack_contribution_sumofsubarrayminimums](coding/freeform_google_coding/monostack_contribution_sumofsubarrayminimums.png) | Sum of Subarray Minimums | LC 907 | Contribution counting with monotonic stack (prev strictly smaller / next smaller-or-equal). |
| [monostack_monotonic_largestrectangleinhistogram](coding/freeform_google_coding/monostack_monotonic_largestrectangleinhistogram.png) | Largest Rectangle in Histogram | LC 84 | Increasing stack of (start_index, height); pop on smaller bar to close rectangles. |
| [monostack_monotonicdeque_slidingwindowmaximum](coding/freeform_google_coding/monostack_monotonicdeque_slidingwindowmaximum.png) | Sliding Window Maximum | LC 239 | Monotonic decreasing deque of indices; pop smaller from back, expired from front, front is the max. |

### prefixsum (5)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [prefixsum_differencearray_carpooling](coding/freeform_google_coding/prefixsum_differencearray_carpooling.png) | Car Pooling | LC 1094 | Difference array +p at start, -p at end; sweep running sum and fail if it exceeds capacity. |
| [prefixsum_differencearray_maximumpopulationyear](coding/freeform_google_coding/prefixsum_differencearray_maximumpopulationyear.png) | Maximum Population Year | LC 1854 | Difference array over years 1950-2050 (+1 birth, -1 death), running sum, track earliest max year. |
| [prefixsum_hashmap_subarraysumequalsk](coding/freeform_google_coding/prefixsum_hashmap_subarraysumequalsk.png) | Subarray Sum Equals K | LC 560 | Count prefix sums in a hashmap seeded {0:1}; add count of (curr_sum - k) each step. |
| [prefixsum_prefixsuffix_productofarrayexceptself](coding/freeform_google_coding/prefixsum_prefixsuffix_productofarrayexceptself.png) | Product of Array Except Self | LC 238 | Single loop multiplying running left prefix and right suffix products into output. |
| [prefixsum_xor_countsubarrayswithgivenxork](coding/freeform_google_coding/prefixsum_xor_countsubarrayswithgivenxork.png) | Count Subarrays with Given XOR K |  | Prefix XOR plus hash map of prefix frequencies, counting freq[prefix ^ k]; analogue of Subarray Sum Equals K. |

### queue (1)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [queue_slidingwindow_movingaveragefromdatastream](coding/freeform_google_coding/queue_slidingwindow_movingaveragefromdatastream.png) | Moving Average from Data Stream | LC 346 | Deque of last k values with running sum; pop oldest when over k, return sum/len in O(1). |

### recursion (3)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [recursion_memo_applysubstitutions](coding/freeform_google_coding/recursion_memo_applysubstitutions.png) | Apply Substitutions | LC 3481 | Resolve %key% placeholders recursively via DFS with memoization over the key dependency graph; O(N). |
| [recursion_parsing_parselispexpression](coding/freeform_google_coding/recursion_parsing_parselispexpression.png) | Parse Lisp Expression | LC 736 | Recursive descent with scoped env dict (copied per let); split tokens only at paren depth 0. |
| [recursion_recursivedescent_evaluatenestedexpressions](coding/freeform_google_coding/recursion_recursivedescent_evaluatenestedexpressions.png) | Evaluate Nested Mathematical Expressions |  | Recursive descent parser with global index for add/sub/mul/div functional notation; O(n) time, O(depth) space |

### slidingwindow (6)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [slidingwindow_fixed_permutationinstring](coding/freeform_google_coding/slidingwindow_fixed_permutationinstring.png) | Permutation in String | LC 567 | Fixed-size window of len(s1) over s2 comparing 26-letter frequency arrays. |
| [slidingwindow_fixed_repeateddnasequences](coding/freeform_google_coding/slidingwindow_fixed_repeateddnasequences.png) | Repeated DNA Sequences | LC 187 | Fixed size-10 window with seen/repeated sets (bitmask rolling hash optional); O(n) |
| [slidingwindow_variable_frequencyofthemostfrequentelement](coding/freeform_google_coding/slidingwindow_variable_frequencyofthemostfrequentelement.png) | Frequency of the Most Frequent Element | LC 1838 | Sort + variable window; cost = nums[r]*len - total, shrink while cost > k. |
| [slidingwindow_variable_longestrepeatingcharacterreplacement](coding/freeform_google_coding/slidingwindow_variable_longestrepeatingcharacterreplacement.png) | Longest Repeating Character Replacement | LC 424 | Sliding window with counts; shrink while window_size - max_count > k; stale max_count is fine. |
| [slidingwindow_variable_longestsubstringwithoutrepeatingcharacters](coding/freeform_google_coding/slidingwindow_variable_longestsubstringwithoutrepeatingcharacters.png) | Longest Substring Without Repeating Characters | LC 3 | Sliding window with char->last-index map; jump left to max(mp[c]+1, l); O(n). |
| [slidingwindow_variable_minimumwindowsubstring](coding/freeform_google_coding/slidingwindow_variable_minimumwindowsubstring.png) | Minimum Window Substring | LC 76 | Variable sliding window with need/window counts and formed==required, shrinking left to minimize. |

### sorting (4)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [sorting_heapsort_sortanarray](coding/freeform_google_coding/sorting_heapsort_sortanarray.png) | Sort an Array | LC 912 | In-place heap sort with max-heap heapify; O(n log n) time, O(1) space. |
| [sorting_mergesort_countinversions](coding/freeform_google_coding/sorting_mergesort_countinversions.png) | Count Inversions |  | Modified merge sort adding (mid - i + 1) cross-half inversions whenever left > right. |
| [sorting_mergesort_countofsmallernumbersafterself](coding/freeform_google_coding/sorting_mergesort_countofsmallernumbersafterself.png) | Count of Smaller Numbers After Self | LC 315 | Merge sort on indices, adding right_count to each left element as it is placed. |
| [sorting_mergesort_mergesortalgorithm](coding/freeform_google_coding/sorting_mergesort_mergesortalgorithm.png) | Merge Sort (Sort an Array) | LC 912 | Recursive divide-and-conquer merge sort with split/merge dry run on [5,2,4,6,1,3]; O(n log n), stable. |

### stack (6)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [stack_callstack_exclusivetimeoffunctions](coding/freeform_google_coding/stack_callstack_exclusivetimeoffunctions.png) | Exclusive Time of Functions | LC 636 | Call stack of function ids + prev_time; credit top on start, inclusive +1 on end, caller resumes at ts+1; O(m) |
| [stack_indices_longestvalidparentheses](coding/freeform_google_coding/stack_indices_longestvalidparentheses.png) | Longest Valid Parentheses | LC 32 | Stack of indices with -1 sentinel boundary; length = i - stack[-1]. |
| [stack_indices_validparenthesisstring](coding/freeform_google_coding/stack_indices_validparenthesisstring.png) | Valid Parenthesis String | LC 678 | Two index stacks for '(' and '*'; ')' pops '(' first else '*'; at the end match leftover '(' with later '*' indices; O(n) time and space |
| [stack_matching_checkwordvalidaftersubstitutions](coding/freeform_google_coding/stack_matching_checkwordvalidaftersubstitutions.png) | Check If Word Is Valid After Substitutions | LC 1003 | Push a/b; on 'c' require top two to be 'b','a' and pop them; valid iff stack empty at end; O(n). |
| [stack_matching_validparentheses](coding/freeform_google_coding/stack_matching_validparentheses.png) | Valid Parentheses | LC 20 | Stack of openers with closing->opening map; mismatch or leftover means invalid; O(n) |
| [stack_nested_decodestring](coding/freeform_google_coding/stack_nested_decodestring.png) | Decode String | LC 394 | Stack of (prev_str, repeat) pushed on '[' and popped on ']' to build curr_str; handle multi-digit counts. |

### string (6)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [string_formatting_formatnumberwithxsignificantdigits](coding/freeform_google_coding/string_formatting_formatnumberwithxsignificantdigits.png) | Format Number with X Significant Digits |  | Split on '.', truncate to X digits (zero-pad integer part if needed), add thousand separators. |
| [string_greedy_licenseplategenerator](coding/freeform_google_coding/string_greedy_licenseplategenerator.png) | License Plate Generator |  | Greedy placement of required chars + fill remaining slots |
| [string_greedy_textjustification](coding/freeform_google_coding/string_greedy_textjustification.png) | Text Justification | LC 68 | Greedily pack words per line, distribute extra spaces left-first, left-justify the last line. |
| [string_hamming_wordswithintwoeditsofdictionary](coding/freeform_google_coding/string_hamming_wordswithintwoeditsofdictionary.png) | Words Within Two Edits of Dictionary | LC 2452 | Brute-force mismatch counting (Hamming distance <= 2) per query vs dictionary; bonus trie DFS. |
| [string_minimax_guesstheword](coding/freeform_google_coding/string_minimax_guesstheword.png) | Guess the Word | LC 843 | Interactive: pick guess minimizing worst-case match-count group, then filter candidates. |
| [string_runlength_stringcompression](coding/freeform_google_coding/string_runlength_stringcompression.png) | Run-Length Encoding (String Compression) |  | Single pass counting consecutive chars, append char+count; O(N) time |

### tree (12)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [tree_bfs_binarytreezigzaglevelordertraversal](coding/freeform_google_coding/tree_bfs_binarytreezigzaglevelordertraversal.png) | Binary Tree Zigzag Level Order Traversal | LC 103 | BFS with None level markers and a deque per level using append/appendleft by direction flag. |
| [tree_degree_findrootthatmakesgraphbinarytree](coding/freeform_google_coding/tree_degree_findrootthatmakesgraphbinarytree.png) | Find a Root That Makes the Graph a Binary Tree |  | Root must have degree <= 2; follow-ups with B/W alternating colors and R/B/W cycle via edge orientation/indegree. |
| [tree_dfs_binarytreeislands](coding/freeform_google_coding/tree_dfs_binarytreeislands.png) | Binary Tree Islands (Count & Sizes) |  | Single-pass DFS with parent_is_one flag; new island starts at a 1 whose parent is 0/None; collect sizes; O(n) |
| [tree_dfs_binarytreemaximumpathsum](coding/freeform_google_coding/tree_dfs_binarytreemaximumpathsum.png) | Binary Tree Maximum Path Sum | LC 124 | Per-node best path = val + left_gain + right_gain, returning max(0, val + max gain) to parent; global max. |
| [tree_dfs_binarytreerightsideview](coding/freeform_google_coding/tree_dfs_binarytreerightsideview.png) | Binary Tree Right Side View | LC 199 | Pre-order DFS visiting right child first, recording first node seen at each depth; left-view variant too. |
| [tree_dfs_binarytreevalueislands](coding/freeform_google_coding/tree_dfs_binarytreevalueislands.png) | Binary Tree Value Islands |  | Same-value connected components via parent-child edges; new island when value differs from parent; counts by value and sizes; O(N) |
| [tree_dfs_diameterofbinarytree](coding/freeform_google_coding/tree_dfs_diameterofbinarytree.png) | Diameter of Binary Tree | LC 543 | Post-order DFS returning height while tracking max left+right depth as the diameter in edges. |
| [tree_dfs_maximumdepthofbinarytree](coding/freeform_google_coding/tree_dfs_maximumdepthofbinarytree.png) | Maximum Depth of Binary Tree | LC 104 | Recursive DFS returning 1 + max(left, right) depth; O(n) time, O(h) space. |
| [tree_dfs_subtreeofanothertree](coding/freeform_google_coding/tree_dfs_subtreeofanothertree.png) | Subtree of Another Tree | LC 572 | For every node in root, check sameTree against subRoot recursively; O(m*n). |
| [tree_postorder_deletenodesandreturnforest](coding/freeform_google_coding/tree_postorder_deletenodesandreturnforest.png) | Delete Nodes And Return Forest | LC 1110 | Postorder DFS with is_root flag; non-deleted children of deleted nodes become new roots; O(n) |
| [tree_serialize_serializeanddeserializebinarytree](coding/freeform_google_coding/tree_serialize_serializeanddeserializebinarytree.png) | Serialize and Deserialize Binary Tree | LC 297 | Preorder DFS with "N" null markers; rebuild via iterator recursion. |
| [tree_xor_findrootofnarytree](coding/freeform_google_coding/tree_xor_findrootofnarytree.png) | Find Root of N-ary Tree | LC 1506 | XOR all node and child values so root survives (O(1) space); alt set of children. |

### trie (10)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [trie_ahocorasick_multipatternstringreplacement](coding/freeform_google_coding/trie_ahocorasick_multipatternstringreplacement.png) | Multi-Pattern String Replacement |  | Trie + BFS fail links + output inheritance; scan once, keep longest whole-word match per start, rebuild string; O(N+M+Z) |
| [trie_ahocorasick_multipatternstringreplacement_v2](coding/freeform_google_coding/trie_ahocorasick_multipatternstringreplacement_v2.png) | Multi-Pattern String Replacement |  | Aho-Corasick: trie + BFS fail links + output lists; one scan, filter whole-token matches, keep longest; O(N+M+Z). |
| [trie_backtracking_wordsearch2](coding/freeform_google_coding/trie_backtracking_wordsearch2.png) | Word Search II | LC 212 | Trie of words + DFS backtracking from each cell, prune non-prefixes, mark visited, null out found words |
| [trie_backtracking_wordsearch2_v2](coding/freeform_google_coding/trie_backtracking_wordsearch2_v2.png) | Word Search II | LC 212 | Build trie of words, DFS each cell following trie children with visited set, collect words at isWord nodes. |
| [trie_dfs_designaddandsearchwordsdatastructure](coding/freeform_google_coding/trie_dfs_designaddandsearchwordsdatastructure.png) | Design Add and Search Words Data Structure | LC 211 | Trie insert; search via DFS where '.' wildcard tries all children. |
| [trie_dfs_designaddandsearchwordsdatastructure_v2](coding/freeform_google_coding/trie_dfs_designaddandsearchwordsdatastructure_v2.png) | Design Add and Search Words Data Structure | LC 211 | Trie insert; search uses DFS that branches over all children on '.' wildcard. |
| [trie_frequency_designautocompletesystem](coding/freeform_google_coding/trie_frequency_designautocompletesystem.png) | Design Search Autocomplete System | LC 642 | Trie nodes store sentences + frequency map; input(c) walks trie, returns top 3 by (-freq, sentence); '#' commits. |
| [trie_pathsegment_httproutematching](coding/freeform_google_coding/trie_pathsegment_httproutematching.png) | HTTP Route Matching |  | Router via segment trie with static children + one param child; static match before param, DFS backtracking |
| [trie_pathtrie_designfilesystem](coding/freeform_google_coding/trie_pathtrie_designfilesystem.png) | Design File System | LC 1166 | Trie keyed by path segments with value per node; createPath requires parent to exist and leaf to be new; get returns -1 if missing. |
| [trie_prefixtree_implementtrieprefixtree](coding/freeform_google_coding/trie_prefixtree_implementtrieprefixtree.png) | Implement Trie (Prefix Tree) | LC 208 | TrieNode with children map + endOfWord; insert/search/startsWith walk characters in O(L). |

### twopointers (6)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [twopointers_greedy_swapadjacentinlrstring](coding/freeform_google_coding/twopointers_greedy_swapadjacentinlrstring.png) | Swap Adjacent in LR String | LC 777 | Two pointers skip X; non-X order must match, L may only move left and R only right. |
| [twopointers_hashset_3sum](coding/freeform_google_coding/twopointers_hashset_3sum.png) | 3Sum | LC 15 | Sort, fix nums[i], hash-set twoSum on the rest, skip duplicates, break when nums[i] > 0. |
| [twopointers_opposite_trappingrainwater](coding/freeform_google_coding/twopointers_opposite_trappingrainwater.png) | Trapping Rain Water | LC 42 | Move the shorter side's pointer, tracking left_max/right_max, O(1) space. |
| [twopointers_opposite_twosum2inputarrayissorted](coding/freeform_google_coding/twopointers_opposite_twosum2inputarrayissorted.png) | Two Sum II - Input Array Is Sorted | LC 167 | Left/right pointers on sorted array, move by sum vs target, return 1-based indices; O(n), O(1) |
| [twopointers_reverse_nextpermutation](coding/freeform_google_coding/twopointers_reverse_nextpermutation.png) | Next Permutation | LC 31 | Find pivot from right, swap with smallest larger element, reverse the suffix in place. |
| [twopointers_sortedcount_dicewinprobability](coding/freeform_google_coding/twopointers_sortedcount_dicewinprobability.png) | Dice Win Probability |  | For each x in sorted A, advance monotonic pointer over sorted B counting b < x; wins/(n*m); O(n+m). |

### unionfind (7)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [unionfind_cycledetection_redundantconnection](coding/freeform_google_coding/unionfind_cycledetection_redundantconnection.png) | Redundant Connection | LC 684 | DSU with path compression + union by rank; first edge whose endpoints share a root is redundant; O(n α(n)) |
| [unionfind_dsu_accountsmerge](coding/freeform_google_coding/unionfind_dsu_accountsmerge.png) | Accounts Merge | LC 721 | Union-find over emails, group by root, sort emails and prepend owner name. |
| [unionfind_dsu_countalienpairsfromdifferentplanets](coding/freeform_google_coding/unionfind_dsu_countalienpairsfromdifferentplanets.png) | Count Alien Pairs from Different Planets |  | Union-find components (planets) by size; count cross-component pairs via running remaining or total minus same-planet. |
| [unionfind_dsu_earliestacquaintancetime](coding/freeform_google_coding/unionfind_dsu_earliestacquaintancetime.png) | The Earliest Moment When Everyone Become Friends | LC 1101 | Sort logs by time, union friends tracking component count; return time when components == 1. |
| [unionfind_dsu_pathwithmaximumminimumvalue](coding/freeform_google_coding/unionfind_dsu_pathwithmaximumminimumvalue.png) | Path With Maximum Minimum Value | LC 1102 | Activate cells high to low, union active neighbors; first value connecting start and end is the answer. |
| [unionfind_nextpointer_rangeassignmentqueries](coding/freeform_google_coding/unionfind_nextpointer_rangeassignmentqueries.png) | Range Assignment Queries on an Array |  | Constant K: difference array; varying K: process queries backwards with DSU next-unprocessed pointer; O(N+Q) |
| [unionfind_overview_disjointsetunion](coding/freeform_google_coding/unionfind_overview_disjointsetunion.png) | Union-Find (Disjoint Set Union) |  | DSU overview: find with path compression, union by size, near-O(1) ops, uses incl. cycle detection and components. |

## prev_2_coding (older)

41 cards · folder `freeform_prev/prev_2_coding`

| Topic | Count |
|---|---|
| dp | 7 |
| backtracking | 5 |
| binarysearch | 5 |
| graph | 3 |
| twopointers | 3 |
| design | 2 |
| hashing | 2 |
| heap | 2 |
| linkedlist | 2 |
| prefixsum | 2 |
| slidingwindow | 2 |
| tree | 2 |
| bst | 1 |
| monostack | 1 |
| stack | 1 |
| string | 1 |

### backtracking (5)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [backtracking_combinations_combinationsum](coding/freeform_prev/prev_2_coding/backtracking_combinations_combinationsum.png) | Combination Sum | LC 39 | Backtrack from start_index, reuse the element (recurse with i), prune when sum > target. |
| [backtracking_constrained_generateparentheses](coding/freeform_prev/prev_2_coding/backtracking_constrained_generateparentheses.png) | Generate Parentheses | LC 22 | Backtrack adding '(' while open<n and ')' while close<open, using DO/RECURSE/UNDO. |
| [backtracking_constrained_nqueens](coding/freeform_prev/prev_2_coding/backtracking_constrained_nqueens.png) | N-Queens | LC 51 | Row-by-row backtracking with col/posDiag/negDiag sets for O(1) attack checks. |
| [backtracking_subsets_subsetsii](coding/freeform_prev/prev_2_coding/backtracking_subsets_subsetsii.png) | Subsets II | LC 90 | Sort, backtrack from start_idx, skip equal neighbours at same depth to avoid duplicate subsets. |
| [backtracking_template_backtrackingblueprint](coding/freeform_prev/prev_2_coding/backtracking_template_backtrackingblueprint.png) | Backtracking Blueprint |  | Generic backtrack template (base case, choices, prune, do/recurse/undo) with state, goal and pruning notes. |

### binarysearch (5)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [binarysearch_answerspace_maximumvalueatagivenindex](coding/freeform_prev/prev_2_coding/binarysearch_answerspace_maximumvalueatagivenindex.png) | Maximum Value at a Given Index in a Bounded Array | LC 1802 | Binary search the peak value; arithmetic-series getsum for left/right sides against maxSum. |
| [binarysearch_answerspace_minimumlimitofballsinabag](coding/freeform_prev/prev_2_coding/binarysearch_answerspace_minimumlimitofballsinabag.png) | Minimum Limit of Balls in a Bag | LC 1760 | Binary search on penalty; ops needed = sum((num-1)//mid) compared to maxOperations. |
| [binarysearch_bisect_findpeakelement](coding/freeform_prev/prev_2_coding/binarysearch_bisect_findpeakelement.png) | Find Peak Element | LC 162 | Binary search comparing nums[mid] vs nums[mid+1] to move toward the peak. |
| [binarysearch_bounds_findfirstandlastpositionofelementinsortedarray](coding/freeform_prev/prev_2_coding/binarysearch_bounds_findfirstandlastpositionofelementinsortedarray.png) | Find First and Last Position of Element in Sorted Array | LC 34 | Two binary searches: round-down mid for the first index, round-up mid for the last. |
| [binarysearch_rotated_searchinrotatedsortedarray](coding/freeform_prev/prev_2_coding/binarysearch_rotated_searchinrotatedsortedarray.png) | Search in Rotated Sorted Array | LC 33 | Binary search: pick the sorted half and check whether target lies in its range. |

### bst (1)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [bst_inorderstack_binarysearchtreeiterator](coding/freeform_prev/prev_2_coding/bst_inorderstack_binarysearchtreeiterator.png) | Binary Search Tree Iterator | LC 173 | Controlled inorder: stack of leftmost path, on next() pop and push left spine of right child. |

### design (2)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [design_ordereddict_lfucache](coding/freeform_prev/prev_2_coding/design_ordereddict_lfucache.png) | LFU Cache | LC 460 | key->(val,freq) map plus freq->OrderedDict buckets with min_freq; evict LRU within min-freq bucket. |
| [design_queuecircular_designhitcounter](coding/freeform_prev/prev_2_coding/design_queuecircular_designhitcounter.png) | Design Hit Counter | LC 362 | Two implementations: deque of timestamps evicting >300s old, and a 300-slot circular array of counts plus times. |

### dp (7)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [dp_knapsack_coinchange](coding/freeform_prev/prev_2_coding/dp_knapsack_coinchange.png) | Coin Change | LC 322 | Unbounded knapsack DP: dp[i] = min(dp[i-c]+1) over coins, -1 if unreachable. |
| [dp_lis_longestincreasingsubsequence](coding/freeform_prev/prev_2_coding/dp_lis_longestincreasingsubsequence.png) | Longest Increasing Subsequence | LC 300 | Patience sorting: bisect_left into tails array, append or replace; return its length. |
| [dp_memo_longestincreasingpathinamatrix](coding/freeform_prev/prev_2_coding/dp_memo_longestincreasingpathinamatrix.png) | Longest Increasing Path in a Matrix | LC 329 | DFS from each cell with memo table over 4 strictly increasing neighbours; O(m*n), with example. |
| [dp_statemachine_minimumoperationstomakecharacterfrequenciesequal](coding/freeform_prev/prev_2_coding/dp_statemachine_minimumoperationstomakecharacterfrequenciesequal.png) | Minimum Operations to Make Character Frequencies Equal | LC 3389 | For each target freq X, run a trash/keep two-state DP across letters a..z with carry-over discounts; take the min. |
| [dp_tabulation_houserobber](coding/freeform_prev/prev_2_coding/dp_tabulation_houserobber.png) | House Robber | LC 198 | Bottom-up DP: dp[i] = max(dp[i-2]+nums[i-1], dp[i-1]). |
| [dp_tabulation_maximumfarefromautonomouspassengerpickup](coding/freeform_prev/prev_2_coding/dp_tabulation_maximumfarefromautonomouspassengerpickup.png) | Maximum Fare From Autonomous Passenger Pickup |  | Right-to-left DP dp[i] = max(skip, 1+0.5d + dp[i+d]) with take[] array to rebuild the chosen pickups. |
| [dp_tabulation_wordbreak](coding/freeform_prev/prev_2_coding/dp_tabulation_wordbreak.png) | Word Break | LC 139 | dp[i] True if some word ends at i and dp[i-len(word)] is True. |

### graph (3)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [graph_bfs_shortestpathinbinarymatrix](coding/freeform_prev/prev_2_coding/graph_bfs_shortestpathinbinarymatrix.png) | Shortest Path in Binary Matrix | LC 1091 | BFS over 8 directions from (0,0) with distance, marking visited cells in the grid. |
| [graph_dfs_numberofislands](coding/freeform_prev/prev_2_coding/graph_dfs_numberofislands.png) | Number of Islands | LC 200 | Grid DFS sinks each land cell, counting one island per DFS start. |
| [graph_topo_coursescheduleii](coding/freeform_prev/prev_2_coding/graph_topo_coursescheduleii.png) | Course Schedule II | LC 210 | Kahn's algorithm: in-degree map, BFS queue of zero in-degree, return order if all courses taken. |

### hashing (2)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [hashing_hashset_validsudoku](coding/freeform_prev/prev_2_coding/hashing_hashset_validsudoku.png) | Valid Sudoku | LC 36 | Row, col and 3x3-box sets via defaultdict(set); a repeated digit means invalid. |
| [hashing_signature_groupshiftedstrings](coding/freeform_prev/prev_2_coding/hashing_signature_groupshiftedstrings.png) | Group Shifted Strings | LC 249 | Key each string by a tuple of cyclic char differences mod 26 in a defaultdict(list). |

### heap (2)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [heap_greedy_minimumnumberofrefuelingstops](coding/freeform_prev/prev_2_coding/heap_greedy_minimumnumberofrefuelingstops.png) | Minimum Number of Refueling Stops | LC 871 | Greedy with max-heap of passed stations' fuel; pop the largest when you can't reach the next position. |
| [heap_prefixsuffix_minimumdifferenceinsumsafterremovalofelements](coding/freeform_prev/prev_2_coding/heap_prefixsuffix_minimumdifferenceinsumsafterremovalofelements.png) | Minimum Difference in Sums After Removal of Elements | LC 2163 | Max-heap prefix of n smallest sums plus min-heap suffix of n largest sums; min over split points. |

### linkedlist (2)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [linkedlist_dummyhead_mergetwosortedlists](coding/freeform_prev/prev_2_coding/linkedlist_dummyhead_mergetwosortedlists.png) | Merge Two Sorted Lists | LC 21 | Dummy head and tail pointer, splice smaller node each step, attach leftover list. |
| [linkedlist_reverse_reversenodesinkgroup](coding/freeform_prev/prev_2_coding/linkedlist_reverse_reversenodesinkgroup.png) | Reverse Nodes in k-Group | LC 25 | Count k nodes, reverse first k iteratively, recursively link head.next to the rest. |

### monostack (1)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [monostack_monotonic_numberofvisiblepeopleinaqueue](coding/freeform_prev/prev_2_coding/monostack_monotonic_numberofvisiblepeopleinaqueue.png) | Number of Visible People in a Queue | LC 1944 | Right-to-left monotonic decreasing stack; count pops plus one if stack non-empty. |

### prefixsum (2)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [prefixsum_bisect_randompickwithweight](coding/freeform_prev/prev_2_coding/prefixsum_bisect_randompickwithweight.png) | Random Pick with Weight | LC 528 | Prefix sums of weights, randint in [1,total], bisect_left to choose the index. |
| [prefixsum_diffarray_zeroarraytransformationi](coding/freeform_prev/prev_2_coding/prefixsum_diffarray_zeroarraytransformationi.png) | Zero Array Transformation I | LC 3355 | Difference array of query coverage; prefix-sum it and check nums[i] <= coverage. |

### slidingwindow (2)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [slidingwindow_variable_longestrepeatingcharacterreplacement](coding/freeform_prev/prev_2_coding/slidingwindow_variable_longestrepeatingcharacterreplacement.png) | Longest Repeating Character Replacement | LC 424 | Window shrinks when window_len - max_freq > k; track max length. |
| [slidingwindow_variable_minimumwindowsubstring](coding/freeform_prev/prev_2_coding/slidingwindow_variable_minimumwindowsubstring.png) | Minimum Window Substring | LC 76 | Expand/contract window with Counter of t and formed/required count; track smallest valid window. |

### stack (1)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [stack_expressioneval_basiccalculator](coding/freeform_prev/prev_2_coding/stack_expressioneval_basiccalculator.png) | Basic Calculator | LC 224 | Running result + sign; push (result, sign) on '(' and pop/combine on ')'. |

### string (1)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [string_simulation_zigzagconversion](coding/freeform_prev/prev_2_coding/string_simulation_zigzagconversion.png) | Zigzag Conversion | LC 6 | Walk rows with a direction flag bouncing at 0 and numRows-1, append chars per row, join. |

### tree (2)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [tree_dfs_pathtotargetnode](coding/freeform_prev/prev_2_coding/tree_dfs_pathtotargetnode.png) | Path to Target Node (Binary Tree) |  | DFS with breadcrumb path list: append, return True if found, else pop; step-by-step breakdown and example. |
| [tree_lca_lowestcommonancestorofabinarytree](coding/freeform_prev/prev_2_coding/tree_lca_lowestcommonancestorofabinarytree.png) | Lowest Common Ancestor of a Binary Tree | LC 236 | Post-order template: return root if p/q, node is LCA when both sides return non-null; with intuition and examples. |

### twopointers (3)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [twopointers_forwardbackward_minimumwindowsubsequence](coding/freeform_prev/prev_2_coding/twopointers_forwardbackward_minimumwindowsubsequence.png) | Minimum Window Subsequence | LC 727 | Card is labelled 76 but the code is Minimum Window Subsequence (LC 727): forward scan to match s2, backward scan to tighten left bound. |
| [twopointers_opposite_squaresofasortedarray](coding/freeform_prev/prev_2_coding/twopointers_opposite_squaresofasortedarray.png) | Squares of a Sorted Array | LC 977 | Left/right pointers fill result from the end with the larger absolute square. |
| [twopointers_skipblanks_swapadjacentinlrstring](coding/freeform_prev/prev_2_coding/twopointers_skipblanks_swapadjacentinlrstring.png) | Move Pieces to Obtain a String | LC 2337 | Two pointers skip '_' in start/target; chars must match, L can't move right, R can't move left (canChange). |

## prev_coding + prev_3_coding (older)

31 cards · folder `freeform_prev`

| Topic | Count |
|---|---|
| graph | 6 |
| tree | 5 |
| stack | 4 |
| design | 3 |
| backtracking | 2 |
| heap | 2 |
| twopointers | 2 |
| binarysearch | 1 |
| dp | 1 |
| hashing | 1 |
| intervals | 1 |
| queue | 1 |
| recursion | 1 |
| unionfind | 1 |

### backtracking (2)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [backtracking_combinations_lettercombinationsofaphonenumber](coding/freeform_prev/prev_coding/backtracking_combinations_lettercombinationsofaphonenumber.png) | Letter Combinations of a Phone Number | LC 17 | Choose/explore/un-choose backtracking over digit-to-letters map with dry run; O(3^n*4^m) |
| [backtracking_dfs_findcheeseinmaze](coding/freeform_prev/prev_coding/backtracking_dfs_findcheeseinmaze.png) | Find Cheese in a Maze |  | Mouse API (isCheese/move) DFS with visited set and physical backtrack via opposite move; O(mn) |

### binarysearch (1)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [binarysearch_bisect_findpeakelement](coding/freeform_prev/prev_3_coding/binarysearch_bisect_findpeakelement.png) | Find Peak Element | LC 162 | Binary search comparing nums[mid] vs nums[mid+1], move toward the rising side; O(log n) |

### design (3)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [design_dll_allo1datastructure](coding/freeform_prev/prev_coding/design_dll_allo1datastructure.png) | All O(1) Data Structure | LC 432 | Sorted doubly linked list of count-buckets + key->node map for O(1) inc/dec/getMaxKey/getMinKey |
| [design_dll_allo1datastructure_v2](coding/freeform_prev/prev_coding/design_dll_allo1datastructure_v2.png) | All O(1) Data Structure | LC 432 | Second version: full inc/dec code for count-node DLL + key_to_node map, with usage example; O(1) ops |
| [design_ordereddict_lrucache](coding/freeform_prev/prev_coding/design_ordereddict_lrucache.png) | LRU Cache | LC 146 | OrderedDict with move_to_end/popitem(last=False) for O(1) get/put, with dry run |

### dp (1)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [dp_lastposition_minimumwindowsubsequence](coding/freeform_prev/prev_coding/dp_lastposition_minimumwindowsubsequence.png) | Minimum Window Subsequence | LC 727 | dp[j] = latest start index in s1 matching s2[0..j], updated right-to-left; O(m*n) time, O(n) space (card's dry-run answer 'bdde' conflicts with stated 'bde') |

### graph (6)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [graph_bfs_wordladder](coding/freeform_prev/prev_coding/graph_bfs_wordladder.png) | Word Ladder | LC 127 | BFS over one-letter-change neighbors with word set and visited set; O(N*L*C) |
| [graph_candidateelimination_findthecelebrity](coding/freeform_prev/prev_coding/graph_candidateelimination_findthecelebrity.png) | Find the Celebrity | LC 277 | Two-pass candidate elimination using knows(a,b) then verification; O(n) time, O(1) space |
| [graph_dfs_clonegraph](coding/freeform_prev/prev_3_coding/graph_dfs_clonegraph.png) | Clone Graph | LC 133 | Recursive DFS with old->clone hashmap to deep-copy nodes and neighbors, handling cycles |
| [graph_dfs_numberofislands](coding/freeform_prev/prev_coding/graph_dfs_numberofislands.png) | Number of Islands | LC 200 | Grid DFS sinking '1' cells to '0', counting components; O(rows*cols) |
| [graph_kruskal_connectingcitieswithminimumcost](coding/freeform_prev/prev_coding/graph_kruskal_connectingcitieswithminimumcost.png) | Connecting Cities With Minimum Cost | LC 1135 | Kruskal MST: sort edges + DSU (path compression, union by rank), -1 if disconnected; O(E log E) |
| [graph_topo_courseschedule2](coding/freeform_prev/prev_coding/graph_topo_courseschedule2.png) | Course Schedule II | LC 210 | Kahn's algorithm (BFS on in-degree) returning course order or [] on cycle; O(V+E) |

### hashing (1)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [hashing_zonemap_maximumnumberoffamiliesinacinema](coding/freeform_prev/prev_3_coding/hashing_zonemap_maximumnumberoffamiliesinacinema.png) | Cinema Seat Allocation | LC 1386 | Map reserved seats per row to blocked zones (2-5, 4-7, 6-9) in a dict of sets; start 2n and subtract per reserved row |

### heap (2)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [heap_topk_kclosestpointstoorigin](coding/freeform_prev/prev_3_coding/heap_topk_kclosestpointstoorigin.png) | K Closest Points to Origin | LC 973 | heapq.nsmallest one-liner plus alternate size-k max-heap with negated squared distances |
| [heap_topk_kclosestpointstoorigin](coding/freeform_prev/prev_coding/heap_topk_kclosestpointstoorigin.png) | K Closest Points to Origin | LC 973 | heapq.nsmallest(k, points, key=squared distance); O(n log k) time, O(k) space |

### intervals (1)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [intervals_interval_mergeintervals](coding/freeform_prev/prev_3_coding/intervals_interval_mergeintervals.png) | Merge Intervals | LC 56 | Sort by start, append non-overlapping interval else extend last end with max; O(n log n) |

### queue (1)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [queue_bfs_nestedlistweightsum2](coding/freeform_prev/prev_coding/queue_bfs_nestedlistweightsum2.png) | Nested List Weight Sum II | LC 364 | BFS level sums over nested list for inverse-depth weighting (card's code/example are inconsistent: resets level_sum, returns 9 vs expected 8) |

### recursion (1)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [recursion_dfs_nestedlistweightsum](coding/freeform_prev/prev_3_coding/recursion_dfs_nestedlistweightsum.png) | Nested List Weight Sum | LC 339 | Recursive DFS summing int*depth over nested list (note: dfs(nested_list,1) gives top-level ints depth 2, off by one) |

### stack (4)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [stack_expressioneval_basiccalculator2](coding/freeform_prev/prev_3_coding/stack_expressioneval_basiccalculator2.png) | Basic Calculator II | LC 227 | Stack of signed terms with last_operator; * and / applied immediately, sum stack at end |
| [stack_pathresolve_simplifypath](coding/freeform_prev/prev_3_coding/stack_pathresolve_simplifypath.png) | Simplify Path | LC 71 | Split on '/', skip ''/'.', pop on '..', push names; join as canonical path |
| [stack_pathresolve_simulateunixcdcommand](coding/freeform_prev/prev_3_coding/stack_pathresolve_simulateunixcdcommand.png) | Simulate Unix cd Command |  | Normalize path, resolve . and .. with a stack, follow symlinks recursively with visited-set cycle detection |
| [stack_twopass_removeinvalidparentheses](coding/freeform_prev/prev_3_coding/stack_twopass_removeinvalidparentheses.png) | Minimum Remove to Make Valid Parentheses | LC 1249 | Two-pass stack: L->R drops extra ')', R->L drops extra '(' (effectively LC 1249 Minimum Remove to Make Valid Parentheses) |

### tree (5)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [tree_bfs_treesideviews](coding/freeform_prev/prev_3_coding/tree_bfs_treesideviews.png) | Tree Side Views |  | BFS level order, collect first (left view) and last (right view) node values per level into a set |
| [tree_dfs_diameterofbinarytree](coding/freeform_prev/prev_coding/tree_dfs_diameterofbinarytree.png) | Diameter of Binary Tree | LC 543 | DFS diameter for N-ary (top two child depths) and binary trees; O(n) time, O(h) space |
| [tree_dfs_findleavesofbinarytree](coding/freeform_prev/prev_coding/tree_dfs_findleavesofbinarytree.png) | Find Leaves of Binary Tree | LC 366 | Post-order DFS grouping nodes by height (null=-1) into res[height]; O(n) time/space |
| [tree_dfs_sumroottoleafnumbers](coding/freeform_prev/prev_3_coding/tree_dfs_sumroottoleafnumbers.png) | Sum Root to Leaf Numbers | LC 129 | DFS carrying curr_num*10+val, return number at leaves and sum left+right |
| [tree_lca_lowestcommonancestor](coding/freeform_prev/prev_3_coding/tree_lca_lowestcommonancestor.png) | Lowest Common Ancestor of a Binary Tree | LC 236 | Recursive binary-tree LCA: return root if both subtrees hit, else the non-None side |

### twopointers (2)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [twopointers_palindrome_validpalindrome2](coding/freeform_prev/prev_3_coding/twopointers_palindrome_validpalindrome2.png) | Valid Palindrome II | LC 680 | Two pointers; on first mismatch check skipping left or right char is a palindrome; O(n) |
| [twopointers_parse_validwordabbreviation](coding/freeform_prev/prev_3_coding/twopointers_parse_validwordabbreviation.png) | Valid Word Abbreviation | LC 408 | Two pointers over word/abbr: parse numbers (reject leading 0) to skip, match letters; end at len(word) |

### unionfind (1)

| Card | Problem | LC | What the card covers |
|---|---|---|---|
| [unionfind_dsu_accountsmerge](coding/freeform_prev/prev_3_coding/unionfind_dsu_accountsmerge.png) | Accounts Merge | LC 721 | DSU over account indices with path compression; email->owner map unions shared emails, group and sort per root |
