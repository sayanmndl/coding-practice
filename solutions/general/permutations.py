from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, nums):
            if i == len(nums):
                res.append(nums[:])
                return

            for idx  in range(i, len(nums)):
                nums[i], nums[idx] = nums[idx], nums[i]
                dfs(i+1, nums)
                nums[i], nums[idx] = nums[idx], nums[i]
        
        dfs(0, nums)
        return res