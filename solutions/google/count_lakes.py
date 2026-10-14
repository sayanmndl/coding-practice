from typing import List

class Solution:
    def countLakes(self, grid: List[List[str]]):
        if not grid or not grid[0]:
            return 0

        rows, cols  = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 'W' or (r,c) in visited:
                return
            
            visited.add((r,c))

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        lakes = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'W' and (r,c) not in visited:
                    lakes += 1
                    dfs(r,c)
        return lakes

grid = [
    ['W', 'W', 'L', 'L'],
    ['W', 'L', 'L', 'W'],
    ['L', 'L', 'W', 'W'],
    ['W', 'L', 'L', 'L']
]

print(Solution().countLakes(grid))
# 3