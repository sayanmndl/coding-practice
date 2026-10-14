class Solution:
    def maxIncreasingSubarrays(self, nums):
        n = len(nums)

        prev = 0 # lenght of prev inc run
        curr = 1 # length of curr inc run
        ans = 0

        for i in range(1,n):
            if nums[i] > nums[i-1]:
                curr+=1
            else:
                # curr inc run ends here
                # 2 subarray within same run
                ans = max(ans, curr//2)

                # one subarray from prev run
                # one from curr
                ans = max(ans, min(prev, curr))

                prev = curr
                curr = 1

        # process the final run
        ans = max(ans, curr//2)
        ans = max(ans, min(prev, curr))
        return ans