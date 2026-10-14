dp_tabulation_dungeongame.png | 174. Dungeon Game | Reverse bottom-up DP for min initial health: dp[i][j]=max(1, min(right,down)-cell).
dp_minimax_stonegame3.png | LeetCode 1406. Stone Game III | Minimax DP on score difference, taking 1-3 stones; sign of dp[0] decides winner.
hashing_counting_findoriginalarrayfromdoubledarray.png | LeetCode 2007. Find Original Array From Doubled Array | Sort + Counter greedy pairing of x with 2x, handling zeros and odd length.
monostack_contribution_sumofsubarrayminimums.png | LeetCode 907 — Sum of Subarray Minimums | Contribution counting with monotonic stack (prev strictly smaller / next smaller-or-equal).
monostack_monotonic_largestrectangleinhistogram.png | LeetCode 84 — Largest Rectangle in Histogram | Increasing stack of (start_index, height); pop on smaller bar to close rectangles.
string_minimax_guesstheword.png | 843. Guess the Word | Interactive: pick guess minimizing worst-case match-count group, then filter candidates.
dp_tabulation_jumpgame2.png | 45. Jump Game II | Right-to-left O(n^2) DP of min jumps to last index (notes greedy O(n) alternative).
sorting_heapsort_sortanarray.png | 912. Sort an Array | In-place heap sort with max-heap heapify; O(n log n) time, O(1) space.
array_cyclicsort_firstmissingpositive.png | First Missing Positive — Cyclic Sort / Index Placement | Place value x at index x-1 by swapping, then scan for first mismatch.
tree_serialize_serializeanddeserializebinarytree.png | 297. Serialize and Deserialize Binary Tree | Preorder DFS with "N" null markers; rebuild via iterator recursion.
linkedlist_fastslow_findtheduplicatenumber.png | Find Duplicate Number — Floyd's Cycle Detection (LeetCode 287) | Treat index->nums[index] as linked list; Floyd meeting point then cycle entrance.
prefixsum_prefixsuffix_productofarrayexceptself.png | Product of Array Except Self — Prefix & Suffix in One Pass | Single loop multiplying running left prefix and right suffix products into output.
matrix_boundary_spiralmatrixandaddtwonumbers.png | 54. Spiral Matrix / 2. Add Two Numbers | Two-problem card: four-boundary spiral traversal, and linked-list digit addition with carry.
design_lazyheap_stockpricefluctuation.png | 2034. Stock Price Fluctuation | Hashmap timestamp->price plus min/max heaps with lazy deletion of stale entries.
heap_kway_mergeksortedlists.png | Merge K Sorted Lists (Min Heap) | K-way merge pushing (val, list_idx, node) into a min-heap; O(N log k).
slidingwindow_variable_frequencyofthemostfrequentelement.png | LeetCode 1838. Frequency of the Most Frequent Element | Sort + variable window; cost = nums[r]*len - total, shrink while cost > k.
graph_bfs_busroutes.png | LeetCode 815 — Bus Routes | BFS over stops with stop->buses map and visited_buses to avoid re-expanding routes.
array_reverse_rotatearray.png | Rotate Array (LeetCode 189) | Rotate right by k via slicing; O(1)-space alternative with three reversals.
math_fastpow_powxn.png | 50. Pow(x, n) | Binary exponentiation by squaring, handling negative exponent via 1/x.
graph_dijkstra_findthesafestpathinagrid.png | LeetCode 2812. Find the Safest Path in a Grid | Multi-source BFS distance to thieves, then max-heap Dijkstra maximizing min safeness.
