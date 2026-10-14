from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        total = 0
        result = 0

        for right in range(len(nums)):
            total+=nums[right]
            # nums[right] * windowsize - total
            while nums[right] * (right-left+1) - total > k:
                total -= nums[left]
                left += 1
            result = max(result, right-left+1)
        return result