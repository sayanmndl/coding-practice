slidingwindow_variable_longestsubstringwithoutrepeatingcharacters.png | 3. Longest Substring Without Repeating Characters | Sliding window with char->last-index map; jump left to max(mp[c]+1, l); O(n).
binarysearch_answer_aggressivecows.png | 139. Aggressive Cows | Binary search on the minimum gap with a greedy placement feasibility check after sorting stalls.
tree_dfs_maximumdepthofbinarytree.png | 104. Maximum Depth of Binary Tree | Recursive DFS returning 1 + max(left, right) depth; O(n) time, O(h) space.
binarysearch_flatten_searcha2dmatrix.png | 74. Search a 2D Matrix | Treat the matrix as a flattened sorted array and binary search with row=mid//cols, col=mid%cols.
tree_dfs_binarytreemaximumpathsum.png | Binary Tree Maximum Path Sum | Per-node best path = val + left_gain + right_gain, returning max(0, val + max gain) to parent; global max.
dp_kadane_maximumproductsubarray.png | Maximum Product Subarray | Kadane variant tracking current max and min product, swapping them on negative numbers.
binarysearch_rotated_searchinrotatedsortedarray.png | Search in Rotated Sorted Array | Binary search that detects which half is sorted and checks whether target lies in it.
heap_topk_topkfrequentelements.png | Top K Frequent Elements | Count frequencies, keep a size-k min-heap of (freq, num); O(n log k), bucket sort alternative.
linkedlist_fastslow_reorderlist.png | 143. Reorder List | Find middle with slow/fast, reverse second half, then merge the two halves alternately in place.
hashing_hashset_validsudoku.png | Valid Sudoku | Hash sets per row, column and 3x3 box (keyed r//3, c//3) to detect duplicate digits.
binarysearch_answer_kokoeatingbananas.png | Koko Eating Bananas (Minimum Eating Speed) | Binary search speed k in [1, max(piles)], checking total ceil(p/k) hours <= h.
tree_bfs_binarytreezigzaglevelordertraversal.png | 103. Binary Tree Zigzag Level Order Traversal | BFS with None level markers and a deque per level using append/appendleft by direction flag.
slidingwindow_variable_longestrepeatingcharacterreplacement.png | 424. Longest Repeating Character Replacement | Sliding window with counts; shrink while window_size - max_count > k; stale max_count is fine.
prefixsum_xor_countsubarrayswithgivenxork.png | 163. Count Subarrays with Given XOR K | Prefix XOR plus hash map of prefix frequencies, counting freq[prefix ^ k]; analogue of Subarray Sum Equals K.
monostack_monotonicdeque_slidingwindowmaximum.png | 239. Sliding Window Maximum | Monotonic decreasing deque of indices; pop smaller from back, expired from front, front is the max.
linkedlist_reverse_reversenodesinkgroup.png | 25. Reverse Nodes in k-Group | Count k nodes ahead, reverse exactly k with a helper, recurse on the rest and link the old head to it.
