# Rename log: prev_coding and prev_3_coding

Format: `folder/newname.png | card title as printed | 1-line content summary`

prev_coding/tree_dfs_diameterofbinarytree.png | DIAMETER OF TREE / BINARY TREE | DFS diameter for N-ary (top two child depths) and binary trees; O(n) time, O(h) space  
prev_coding/tree_dfs_findleavesofbinarytree.png | FIND LEAVES OF BINARY TREE | Post-order DFS grouping nodes by height (null=-1) into res[height]; O(n) time/space  
prev_coding/backtracking_dfs_findcheeseinmaze.png | FIND CHEESE IN A MAZE USING DFS (BACKTRACKING) | Mouse API (isCheese/move) DFS with visited set and physical backtrack via opposite move; O(mn)  
prev_coding/graph_topo_courseschedule2.png | COURSE SCHEDULE II | Kahn's algorithm (BFS on in-degree) returning course order or [] on cycle; O(V+E)  
prev_coding/queue_bfs_nestedlistweightsum2.png | NESTED LIST WEIGHT SUM II | BFS level sums over nested list for inverse-depth weighting (card's code/example are inconsistent: resets level_sum, returns 9 vs expected 8)  
prev_coding/graph_candidateelimination_findthecelebrity.png | FIND THE CELEBRITY | Two-pass candidate elimination using knows(a,b) then verification; O(n) time, O(1) space  
prev_coding/backtracking_combinations_lettercombinationsofaphonenumber.png | LETTER COMBINATIONS OF A PHONE NUMBER | Choose/explore/un-choose backtracking over digit-to-letters map with dry run; O(3^n*4^m)  
prev_coding/graph_kruskal_connectingcitieswithminimumcost.png | MINIMUM COST TO CONNECT ALL CITIES | Kruskal MST: sort edges + DSU (path compression, union by rank), -1 if disconnected; O(E log E)  
prev_coding/heap_topk_kclosestpointstoorigin.png | K CLOSEST POINTS TO ORIGIN | heapq.nsmallest(k, points, key=squared distance); O(n log k) time, O(k) space  
prev_coding/graph_dfs_numberofislands.png | NUMBER OF ISLANDS | Grid DFS sinking '1' cells to '0', counting components; O(rows*cols)  
prev_coding/design_dll_allo1datastructure.png | ALL O(1) DATA STRUCTURE | Sorted doubly linked list of count-buckets + key->node map for O(1) inc/dec/getMaxKey/getMinKey  
prev_coding/design_ordereddict_lrucache.png | LRU CACHE (Least Recently Used) | OrderedDict with move_to_end/popitem(last=False) for O(1) get/put, with dry run  
prev_coding/dp_lastposition_minimumwindowsubsequence.png | MINIMUM WINDOW SUBSEQUENCE (DP - LAST POSITION) | dp[j] = latest start index in s1 matching s2[0..j], updated right-to-left; O(m*n) time, O(n) space (card's dry-run answer 'bdde' conflicts with stated 'bde')  
prev_coding/design_dll_allo1datastructure_v2.png | ALL O(1) DATA STRUCTURE | Second version: full inc/dec code for count-node DLL + key_to_node map, with usage example; O(1) ops  
prev_coding/graph_bfs_wordladder.png | WORD LADDER (LENGTH OF SHORTEST TRANSFORMATION) | BFS over one-letter-change neighbors with word set and visited set; O(N*L*C)  
prev_3_coding/stack_expressioneval_basiccalculator2.png | Basic Calculator ( + - * / ) | Stack of signed terms with last_operator; * and / applied immediately, sum stack at end  
prev_3_coding/tree_lca_lowestcommonancestor.png | LOWEST COMMON ANCESTOR | Recursive binary-tree LCA: return root if both subtrees hit, else the non-None side  
prev_3_coding/binarysearch_bisect_findpeakelement.png | Find Peak Element | Binary search comparing nums[mid] vs nums[mid+1], move toward the rising side; O(log n)  
prev_3_coding/hashing_zonemap_maximumnumberoffamiliesinacinema.png | Maximum Number of Families in a Cinema | Map reserved seats per row to blocked zones (2-5, 4-7, 6-9) in a dict of sets; start 2n and subtract per reserved row  
prev_3_coding/recursion_dfs_nestedlistweightsum.png | Nested Depth Sum | Recursive DFS summing int*depth over nested list (note: dfs(nested_list,1) gives top-level ints depth 2, off by one)  
prev_3_coding/twopointers_parse_validwordabbreviation.png | VALID WORD ABBREVIATION PROBLEM | Two pointers over word/abbr: parse numbers (reject leading 0) to skip, match letters; end at len(word)  
prev_3_coding/heap_topk_kclosestpointstoorigin.png | K Closest Points to Origin | heapq.nsmallest one-liner plus alternate size-k max-heap with negated squared distances  
prev_3_coding/stack_twopass_removeinvalidparentheses.png | Remove Invalid Parentheses | Two-pass stack: L->R drops extra ')', R->L drops extra '(' (effectively LC 1249 Minimum Remove to Make Valid Parentheses)  
prev_3_coding/intervals_interval_mergeintervals.png | Merge Intervals | Sort by start, append non-overlapping interval else extend last end with max; O(n log n)  
prev_3_coding/stack_pathresolve_simulateunixcdcommand.png | Simulate Unix cd Command | Normalize path, resolve . and .. with a stack, follow symlinks recursively with visited-set cycle detection  
prev_3_coding/tree_dfs_sumroottoleafnumbers.png | Sum Root to Leaf Numbers | DFS carrying curr_num*10+val, return number at leaves and sum left+right  
prev_3_coding/stack_pathresolve_simplifypath.png | SIMPLIFY PATH | Split on '/', skip ''/'.', pop on '..', push names; join as canonical path  
prev_3_coding/graph_dfs_clonegraph.png | Clone Graph | Recursive DFS with old->clone hashmap to deep-copy nodes and neighbors, handling cycles  
prev_3_coding/twopointers_palindrome_validpalindrome2.png | Valid Palindrome II | Two pointers; on first mismatch check skipping left or right char is a palindrome; O(n)  
prev_3_coding/unionfind_dsu_accountsmerge.png | Accounts Merge using Union Find | DSU over account indices with path compression; email->owner map unions shared emails, group and sort per root  
prev_3_coding/tree_bfs_treesideviews.png | TREE SIDE VIEWS | BFS level order, collect first (left view) and last (right view) node values per level into a set  
