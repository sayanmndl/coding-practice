dp_tabulation_houserobber.png | 198. House Robber | Bottom-up DP: dp[i] = max(dp[i-2]+nums[i-1], dp[i-1]).
twopointers_opposite_squaresofasortedarray.png | Squares of a Sorted Array | Left/right pointers fill result from the end with the larger absolute square.
twopointers_skipblanks_swapadjacentinlrstring.png | Swap Adjacent in LR String | Two pointers skip '_' in start/target; chars must match, L can't move right, R can't move left (canChange).
slidingwindow_variable_minimumwindowsubstring.png | 76. Minimum Window Substring | Expand/contract window with Counter of t and formed/required count; track smallest valid window.
dp_lis_longestincreasingsubsequence.png | 300. Longest Increasing Subsequence | Patience sorting: bisect_left into tails array, append or replace; return its length.
string_simulation_zigzagconversion.png | Zigzag Conversion | Walk rows with a direction flag bouncing at 0 and numRows-1, append chars per row, join.
design_ordereddict_lfucache.png | 460. LFU Cache | key->(val,freq) map plus freq->OrderedDict buckets with min_freq; evict LRU within min-freq bucket.
slidingwindow_variable_longestrepeatingcharacterreplacement.png | 424. Longest Repeating Character Replacement | Window shrinks when window_len - max_freq > k; track max length.
backtracking_subsets_subsetsii.png | 90. Subsets II | Sort, backtrack from start_idx, skip equal neighbours at same depth to avoid duplicate subsets.
stack_expressioneval_basiccalculator.png | 224. Basic Calculator | Running result + sign; push (result, sign) on '(' and pop/combine on ')'.
bst_inorderstack_binarysearchtreeiterator.png | 173. Binary Search Tree Iterator | Controlled inorder: stack of leftmost path, on next() pop and push left spine of right child.
monostack_monotonic_numberofvisiblepeopleinaqueue.png | 1944. Number of Visible People in a Queue | Right-to-left monotonic decreasing stack; count pops plus one if stack non-empty.
binarysearch_bisect_findpeakelement.png | 162. Find Peak Element | Binary search comparing nums[mid] vs nums[mid+1] to move toward the peak.
tree_lca_lowestcommonancestorofabinarytree.png | Lowest Common Ancestor (Binary Tree) | Post-order template: return root if p/q, node is LCA when both sides return non-null; with intuition and examples.
twopointers_forwardbackward_minimumwindowsubsequence.png | 76. Minimum Window Substring | Card is labelled 76 but the code is Minimum Window Subsequence (LC 727): forward scan to match s2, backward scan to tighten left bound.
graph_bfs_shortestpathinbinarymatrix.png | Shortest Path in Binary Matrix | BFS over 8 directions from (0,0) with distance, marking visited cells in the grid.
tree_dfs_pathtotargetnode.png | Path to Target Node (Binary Tree) | DFS with breadcrumb path list: append, return True if found, else pop; step-by-step breakdown and example.
binarysearch_answerspace_minimumlimitofballsinabag.png | Minimum Limit of Balls in a Bag | Binary search on penalty; ops needed = sum((num-1)//mid) compared to maxOperations.
linkedlist_dummyhead_mergetwosortedlists.png | Merge Two Sorted Lists | Dummy head and tail pointer, splice smaller node each step, attach leftover list.
dp_knapsack_coinchange.png | 322. Coin Change | Unbounded knapsack DP: dp[i] = min(dp[i-c]+1) over coins, -1 if unreachable.
backtracking_constrained_generateparentheses.png | 22. Generate Parentheses | Backtrack adding '(' while open<n and ')' while close<open, using DO/RECURSE/UNDO.
dp_memo_longestincreasingpathinamatrix.png | Longest Increasing Path in a Matrix (DFS + Memoization) | DFS from each cell with memo table over 4 strictly increasing neighbours; O(m*n), with example.
binarysearch_rotated_searchinrotatedsortedarray.png | Search in Rotated Sorted Array | Binary search: pick the sorted half and check whether target lies in its range.
design_queuecircular_designhitcounter.png | Design Hit Counter | Two implementations: deque of timestamps evicting >300s old, and a 300-slot circular array of counts plus times.
linkedlist_reverse_reversenodesinkgroup.png | Reverse Nodes in k-Group | Count k nodes, reverse first k iteratively, recursively link head.next to the rest.
hashing_signature_groupshiftedstrings.png | Group Shifted Strings | Key each string by a tuple of cyclic char differences mod 26 in a defaultdict(list).
dp_statemachine_minimumoperationstomakecharacterfrequenciesequal.png | 3389. Minimum Operations to Make Character Frequencies Equal | For each target freq X, run a trash/keep two-state DP across letters a..z with carry-over discounts; take the min.
dp_tabulation_maximumfarefromautonomouspassengerpickup.png | Maximum Fare From Autonomous Passenger Pickup | Right-to-left DP dp[i] = max(skip, 1+0.5d + dp[i+d]) with take[] array to rebuild the chosen pickups.
heap_prefixsuffix_minimumdifferenceinsumsafterremovalofelements.png | 2163. Minimum Difference in Sums After Removal of Elements | Max-heap prefix of n smallest sums plus min-heap suffix of n largest sums; min over split points.
binarysearch_answerspace_maximumvalueatagivenindex.png | Maximum Value at a Given Index | Binary search the peak value; arithmetic-series getsum for left/right sides against maxSum.
backtracking_combinations_combinationsum.png | 39. Combination Sum | Backtrack from start_index, reuse the element (recurse with i), prune when sum > target.
graph_topo_coursescheduleii.png | 210. Course Schedule II | Kahn's algorithm: in-degree map, BFS queue of zero in-degree, return order if all courses taken.
binarysearch_bounds_findfirstandlastpositionofelementinsortedarray.png | Find First and Last Position of Element in Sorted Array | Two binary searches: round-down mid for the first index, round-up mid for the last.
graph_dfs_numberofislands.png | 200. Number of Islands | Grid DFS sinks each land cell, counting one island per DFS start.
dp_tabulation_wordbreak.png | 139. Word Break | dp[i] True if some word ends at i and dp[i-len(word)] is True.
prefixsum_bisect_randompickwithweight.png | 528. Random Pick with Weight | Prefix sums of weights, randint in [1,total], bisect_left to choose the index.
backtracking_template_backtrackingblueprint.png | Backtracking Blueprint | Generic backtrack template (base case, choices, prune, do/recurse/undo) with state, goal and pruning notes.
heap_greedy_minimumnumberofrefuelingstops.png | 871. Minimum Number of Refueling Stops | Greedy with max-heap of passed stations' fuel; pop the largest when you can't reach the next position.
prefixsum_diffarray_zeroarraytransformationi.png | 3355. Zero Array Transformation I | Difference array of query coverage; prefix-sum it and check nums[i] <= coverage.
backtracking_constrained_nqueens.png | 51. N-Queens | Row-by-row backtracking with col/posDiag/negDiag sets for O(1) attack checks.
hashing_hashset_validsudoku.png | Valid Sudoku | Row, col and 3x3-box sets via defaultdict(set); a repeated digit means invalid.
