intervals_greedy_nonoverlappingintervals_v2.png | Erase Overlap Intervals | Sort by start; on overlap count a removal and keep the smaller end (prevEnd=min); O(n log n) time, O(1) space
dp_lis_longestincreasingsubsequence_v2.png | Longest Increasing Subsequence (LIS) | Patience sorting tails + bisect_left O(n log n), plus O(n^2) DP LIS[i]=1+max LIS[j] for j>i with nums[j]>nums[i]; O(n) space
dp_tabulation_distinctsubsequences.png | Distinct Subsequences | 2D DP dp[i][j]=ways to form t[j:] from s[i:]: skip s[i] + (match ? dp[i+1][j+1]); dp[i][n]=1; O(mn) time/space, O(n) with 1D
bitmanip_fulladder_sumoftwointegers.png | Sum of Two Integers | Bit-by-bit full adder over 32 bits with 32-bit mask, convert back via ~(res ^ mask) if sign bit set; O(1) time/space
dp_tabulation_mincostclimbingstairs.png | Min Cost Climbing Stairs | dp[i]=min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2]), dp[0]=dp[1]=0, answer dp[n]; O(n) time, O(1) with two vars
dp_tabulation_editdistance.png | Edit Distance | Suffix 2D DP: match -> dp[i+1][j+1], else 1+min(delete, insert, replace); bases dp[m][j]=n-j, dp[i][n]=m-i; O(mn) time/space, O(n) rolling
dp_tabulation_jumpgame2_v2.png | Jump Game II | Right-to-left DP dp[i]=1+min dp[j] for j in (i, i+nums[i]], dp[n-1]=0; O(n^2) time, O(n) space (greedy O(n) mentioned)
dp_interval_burstballoons.png | Burst Balloons | Interval DP, pad with 1s, pick i as LAST balloon in [l,r]: dp[l][r]=max(new[l-1]*new[i]*new[r+1]+dp[l][i-1]+dp[i+1][r]); O(n^3) time, O(n^2) space
greedy_lastindex_partitionlabels.png | Partition Labels | Record last index of each char; scan extending end=max(end,last[c]) and cut when i==end; O(n) time, O(1) space
dp_statemachine_besttimetobuyandsellstockwithcooldown.png | Best Time to Buy and Sell Stock with Cooldown | State DP from right to left: dp[i][buy]=max(-p+dp[i+1][hold], dp[i+1][buy]); dp[i][hold]=max(p+dp[i+2][buy], dp[i+1][hold]); O(n) time, O(1) with 3 vars
greedy_filter_mergetripletstoformtargettriplet.png | Merge Triplets | Skip any triplet exceeding target in some slot; among the rest, record which positions hit target exactly; true if all 3 hit; O(n) time, O(1) space
greedy_runningsum_gasstation.png | Gas Station | If sum(gas)<sum(cost) return -1; else one pass with running tank, reset tank and set start=i+1 whenever it goes negative; O(n) time, O(1) space
dp_knapsack_coinchange2.png | Coin Change II | Unbounded knapsack counting: dp[i][a]=dp[i+1][a]+dp[i][a-coin]; 1D version loops coins outer, amount inner ascending (dp[a]+=dp[a-coin]); O(n*amount) time, O(amount) space
dp_tabulation_interleavingstring.png | Interleaving String | Suffix 2D DP dp[i][j]=(s1[i]==s3[i+j] and dp[i+1][j]) or (s2[j]==s3[i+j] and dp[i][j+1]), dp[m][n]=True, length check first; O(mn) time, O(n) possible
