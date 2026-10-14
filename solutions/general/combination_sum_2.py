from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, path, total):
            if total == target:
                res.append(path[:])
                return
            for idx in range(i, len(candidates)):
                if idx > i and candidates[idx] == candidates[idx-1]:
                    continue
                if total + candidates[idx] > target:
                    break
                path.append(candidates[idx])
                dfs(idx+1, path, total + candidates[idx])
                path.pop()

        dfs(0,[],0)
        return res