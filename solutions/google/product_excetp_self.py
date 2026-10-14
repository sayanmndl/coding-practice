class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        output = [1]*n
        left , right = 1,1
        for i in range(n):
            output[i] *= left
            left *= nums[i]
            output[-1-i] *= right
            right *= nums[-1-i]
        return output