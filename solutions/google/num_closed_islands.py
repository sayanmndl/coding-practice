class Solution:
    def closedIsland(self, grid):
        m,n = len(grid), len(grid[0])

        def dfs(r , c):
            if ( r < 0 or r >= m or c < 0 or c >=n or grid[r][c] == 1):
                return True
            
            # mark land as visited/water
            grid[r][c] == 1

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r, c+1)
            dfs(r, c-1)

        # remove all land connected to the boundary

        # left and right boundaries
        for r in range(m):
            if grid[r][0] == 0:
                dfs(r, 0)

            if grid[r][n-1] == 0:
                dfs(r, n-1)
        
        # top and bottom boundaries
        for c in range(n):
            if grid[0][c] == 0:
                dfs(0, c)
            if grid[m-1][c]==0:
                dfs(m-1,c)

        count = 0
        for r in range(1, m-1):
            for c in range(1, n-1):
                if grid[r][c] == 0:
                    count+=1
                    dfs(r,c)
        return count

        