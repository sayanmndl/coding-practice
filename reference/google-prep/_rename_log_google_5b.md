binarysearch_answer_splitarraylargestsum.png | 309. Split Array - Largest Sum | Binary search on the answer in [max(a), sum(a)] with a greedy split-count feasibility check.
sorting_mergesort_mergesortalgorithm.png | Merge Sort Algorithm | Recursive divide-and-conquer merge sort with split/merge dry run on [5,2,4,6,1,3]; O(n log n), stable.
slidingwindow_fixed_permutationinstring.png | 567. Permutation in String | Fixed-size window of len(s1) over s2 comparing 26-letter frequency arrays.
sorting_mergesort_countinversions.png | 131. Count Inversions | Modified merge sort adding (mid - i + 1) cross-half inversions whenever left > right.
tree_dfs_diameterofbinarytree.png | 543. Diameter of Binary Tree | Post-order DFS returning height while tracking max left+right depth as the diameter in edges.
tree_dfs_binarytreerightsideview.png | 199. Binary Tree Right Side View | Pre-order DFS visiting right child first, recording first node seen at each depth; left-view variant too.
bst_bounds_validatebinarysearchtree.png | Validate Binary Search Tree (LeetCode 98) | DFS passing (low, high) bounds down the tree with strict inequality checks.
greedy_counting_taskscheduler_v2.png | Task Scheduler | Counting formula max(len(tasks), (f-1)*(n+1)+count) plus max-heap + cooldown-queue simulation alternative.
linkedlist_hashmap_copylistwithrandompointer.png | 138. Copy List with Random Pointer | Recursive deep copy using an original-to-copy hash map to reuse nodes and handle cycles.
design_hashmapdll_lrucache.png | 146. LRU Cache | Hash map + doubly linked list with dummy head/tail for O(1) get/put and LRU eviction.
binarysearch_partition_medianoftwosortedarrays.png | 27. Median of 2 Sorted Arrays | Binary search a partition on the smaller array so left halves total (m+n+1)//2 and are all <= right halves.
bst_lca_lowestcommonancestorofabinarysearchtree.png | 235. Lowest Common Ancestor of a Binary Search Tree | Iteratively walk from root using BST ordering until p and q split; O(h) time, O(1) space.
slidingwindow_variable_minimumwindowsubstring.png | 76. Minimum Window Substring | Variable sliding window with need/window counts and formed==required, shrinking left to minimize.
linkedlist_reverse_reverselinkedlist.png | 206. Reverse Linked List | Iterative prev/curr/temp pointer reversal with step-by-step walkthrough.
tree_dfs_subtreeofanothertree.png | 572. Subtree of Another Tree | For every node in root, check sameTree against subRoot recursively; O(m*n).
