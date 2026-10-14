dp_knapsack_partitionequalsubsetsum.png | Partition Equal Subset Sum (LC 416) | 0/1 subset-sum DP to target=sum/2, 2D table plus 1D backwards version; O(n*target) time, O(target) space
greedy_counting_handofstraights.png | Hand of Straights (LC 846) | Counter + walk back to smallest start of each consecutive run, greedily peel groups of size k; O(n) amortized (card says O(n log n)), O(n) space
dp_knapsack_coinchange_v2.png | Coin Change (LC 322) | Unbounded-knapsack bottom-up dp[a]=min(1+dp[a-c]) with amount+1 as infinity, plus top-down lru_cache version; O(amount*n) time, O(amount) space
bitmanip_shift_reversebits.png | Reverse Bits (LC 190) | Loop 32 times: take bit i with (n>>i)&1 and add it at position 31-i; O(1) time and space
dp_tabulation_decodeways.png | Decode Ways (LC 91) | Right-to-left DP: dp[i]=dp[i+1] if s[i]!='0', plus dp[i+2] if s[i:i+2] is 10-26; O(n) time, O(n) or O(1) with two variables
dp_hashmap_targetsum.png | Target Sum (LC 494) | Layer-by-layer DP over a hashmap of reachable sums -> ways (add and subtract each num), O(S) space variant; O(n*S) time
graph_dijkstra_swiminrisingwater.png | Swim in Rising Water (LC 778) | Minimax Dijkstra: min-heap keyed by max elevation on path so far, return when bottom-right is popped; O(n^2 log n) time, O(n^2) space
dp_tabulation_uniquepaths.png | Unique Paths (LC 62) | Grid DP from bottom-right: dp[i][j]=dp[i+1][j]+dp[i][j+1], 1D row version, plus C(m+n-2, m-1) formula; O(m*n) time, O(n) space
matrix_transpose_rotateimage.png | Rotate Image (LC 48) | Transpose across the main diagonal, then reverse each row; O(n^2) time, O(1) space
dp_tabulation_houserobber1and2.png | House Robber (LC 198) + House Robber II (LC 213) | dp[i]=max(dp[i-1], nums[i]+dp[i-2]) with an O(1) two-variable version; II runs it twice on nums[1:] and nums[:-1]; O(n) time
dp_tabulation_longestcommonsubsequence.png | Longest Common Subsequence (LC 1143) | Suffix DP: match -> 1+dp[i+1][j+1], else max(dp[i+1][j], dp[i][j+1]), plus rolling 1D row; O(m*n) time, O(n) space
stack_indices_validparenthesisstring.png | Valid Parenthesis String (LC 678) | Two index stacks for '(' and '*'; ')' pops '(' first else '*'; at the end match leftover '(' with later '*' indices; O(n) time and space
dp_memo_longestincreasingpathinamatrix_v2.png | Longest Increasing Path in a Matrix (LC 329) | Memoized DFS from every cell passing prevVal, recurse only into strictly larger neighbors, answer = max memo value; O(m*n) time and space
matrix_markers_setmatrixzeroes.png | Set Matrix Zeroes (LC 73) | Use first row/column as zero markers plus a zeroInFirstCol flag, then fill bottom-right to top-left; O(mn) time, O(1) space
