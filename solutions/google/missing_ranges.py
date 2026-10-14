class Solution:
    def findMissingRanges(self, nums, lower, upper):
        result = []
        prev = lower - 1 # pretend theres value before lower

        # 0 -> n+1
        for i in range(len(nums) + 1):
            curr = nums[i] if i < len(nums) else upper + 1 # we've reached the end so pick upper + 1
            
            # if there is atleast 1 missing number between prev and curr record it
            if curr - prev > 1:
                result.append([prev+1, curr-1])
            
            prev = curr

        return result