backtracking_swap_permutations.png | Permutations | Backtracking by in-place swapping nums[i] with nums[idx], recurse i+1, swap back; O(n·n!).
backtracking_partition_palindromepartitioning.png | Palindrome Partitioning | Backtrack over cut end-index j, recurse on j+1 when s[i:j+1] is a palindrome (two-pointer check).
backtracking_dfs_wordsearch_v2.png | Word Search | DFS from every cell, mark visited with '#', explore 4 neighbors, restore on backtrack; O(R·C·3^L).
graph_multisourcebfs_wallsandgates_v2.png | Walls and Gates (Islands and Treasure) | Multi-source BFS from all gates level by level, writing distance into empty rooms.
graph_dfs_surroundedregions.png | Surrounded Regions | DFS from border 'O's marking them 'T', then flip remaining 'O' to 'X' and restore 'T' to 'O'.
trie_prefixtree_implementtrieprefixtree.png | Implement Trie (Prefix Tree) | TrieNode with children map + endOfWord; insert/search/startsWith walk characters in O(L).
backtracking_dedup_subsets2.png | Subsets II | Sort, add subset at every level, skip nums[j]==nums[j-1] when j>i to avoid duplicate subsets.
graph_topo_courseschedule.png | Course Schedule | Kahn's BFS topological sort with indegrees; possible iff all courses get processed.
graph_dfs_redundantconnection.png | Redundant Connection | DFS with parent tracking to collect cycle nodes, then return last edge (reverse scan) with both endpoints in the cycle.
graph_bfs_graphvalidtree.png | Valid Tree | Reject if edges > n-1, BFS with parent to detect cycles, then require all n nodes visited.
trie_dfs_designaddandsearchwordsdatastructure_v2.png | Design Add and Search Words Data Structure | Trie insert; search uses DFS that branches over all children on '.' wildcard.
trie_backtracking_wordsearch2_v2.png | Word Search II | Build trie of words, DFS each cell following trie children with visited set, collect words at isWord nodes.
backtracking_dfs_combinationsum.png | Combination Sum | Include/exclude DFS: include nums[i] staying at i (reuse), exclude moves to i+1; prune when total > target.
backtracking_sets_nqueens.png | N-Queens | Row-by-row backtracking with column, r+c and r-c sets to check safety; O(n!).
graph_dfs_maxareaofisland.png | Max Area of Island | Recursive DFS returning 1 + sum of 4 neighbors with a visited set; track max over all land cells.
backtracking_includeexclude_subsets.png | Subsets | Binary include/exclude recursion on each index, append copy at i==n; 2^n subsets, O(n·2^n).
backtracking_counting_generateparentheses.png | Generate Parentheses | Backtrack adding '(' while open<n and ')' while close<open; count is the nth Catalan number.
