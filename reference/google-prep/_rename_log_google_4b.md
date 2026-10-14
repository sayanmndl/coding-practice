greedy_differencearray_minimumnumberofincrementsonsubarraystoformatargetarray.png | LeetCode 1526. Minimum Number of Increments on Subarrays to Form a Target Array | Answer = target[0] + sum of positive adjacent differences (histogram layers view).
dp_tabulation_regularexpressionmatching.png | 10. Regular Expression Matching | 2D DP over s/p with '.' and '*' transitions (zero vs one-or-more occurrences), worked table.
matrix_simulation_spiralmatrix.png | Spiral Order Traversal (Spiral Matrix) - Boundary Simulation | Four shrinking boundaries, traverse top/right/bottom/left with up!=down and left!=right guards.
string_greedy_textjustification.png | 68. Text Justification | Greedily pack words per line, distribute extra spaces left-first, left-justify the last line.
twopointers_reverse_nextpermutation.png | LeetCode 31. Next Permutation | Find pivot from right, swap with smallest larger element, reverse the suffix in place.
stack_indices_longestvalidparentheses.png | LeetCode 32. Longest Valid Parentheses | Stack of indices with -1 sentinel boundary; length = i - stack[-1].
dp_tabulation_minimumtimetofinishtherace.png | 2188. Minimum Time to Finish the Race | Precompute best[k] for k consecutive laps per tire, then dp[i] = min(dp[i-k] + changeTime + best[k]).
twopointers_opposite_trappingrainwater.png | Trapping Rain Water - Two Pointers (LeetCode 42) | Move the shorter side's pointer, tracking left_max/right_max, O(1) space.
dp_kadane_maximumsubarray.png | Maximum Subarray (LeetCode 53) | dp[i] = max(nums[i], dp[i-1]+nums[i]); Kadane's O(1)-space version.
prefixsum_hashmap_subarraysumequalsk.png | Subarray Sum Equals K (LeetCode 560) | Count prefix sums in a hashmap seeded {0:1}; add count of (curr_sum - k) each step.
dp_prefixsum_numberofzigzagarrays1.png | 3699. Number of ZigZag Arrays I | up[j]/down[j] DP by last direction, transitions via prefix/suffix sums for O(n*k).
sorting_mergesort_countofsmallernumbersafterself.png | LeetCode 315. Count of Smaller Numbers After Self | Merge sort on indices, adding right_count to each left element as it is placed.
dp_interval_longestpalindromicsubstring.png | Longest Palindromic Substring | dp[i][j] palindrome table: s[i]==s[j] and (len 2 or dp[i+1][j-1]); O(n^2).
hashing_hashset_longestconsecutivesequence.png | Longest Consecutive Sequence (LeetCode 128) | Hash set, start counting only at sequence starts (n-1 not in set), O(n).
array_boyermoore_majorityelement.png | LeetCode 169. Majority Element | Boyer-Moore voting with candidate and count, O(n) time O(1) space.
design_bisect_snapshotarray.png | 1146. Snapshot Array | Per-index history of (snap_id, value); bisect_right for get, overwrite on repeated set in same snap.
twopointers_hashset_3sum.png | 3Sum (LeetCode 15) | Sort, fix nums[i], hash-set twoSum on the rest, skip duplicates, break when nums[i] > 0.
linkedlist_mergesort_sortlist.png | 148. Sort List | Merge sort on linked list: fast/slow split (fast=head.next), recurse, merge with dummy node.
design_bisect_timebasedkeyvaluestore.png | LeetCode 981. Time Based Key-Value Store | Hashmap key -> sorted (timestamp, value) list; binary search for rightmost timestamp <= target.
