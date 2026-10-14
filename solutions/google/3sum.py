
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i==0 or nums[i-1] != nums[i]:
                self.twoSum(nums,i)
        return self.res


    def twoSum(self, nums, i):
        seen = set()
        j = i + 1
        while j < len(nums):
            rem = -nums[i]-nums[j]
            if rem in seen:
                self.res.append((nums[i], nums[j], rem))
                while j+1 < len(nums) and nums[j] == nums[j+1]:
                    j+=1
            seen.add(nums[j])
            j+=1