
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if not nums: return 0

        n = len(nums)
        dp = [-float('inf')]*n
        dp[0] = nums[0]
        max_sum = dp[0]

        for i in range(1,n):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
        
        return max(dp)