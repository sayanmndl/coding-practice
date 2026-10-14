from collections import deque

class Solution:
    def islandsAndTreasure(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))

        directions = [
            (1,0), (-1,0), (0,1), (0,-1)
        ]

        while queue:
            r,c = queue.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if ( 0 <= nr < rows and 0<= nc < cols and grid[nr][nc] == 2147483647):
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr,nc))

