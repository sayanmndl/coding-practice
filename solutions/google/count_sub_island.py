class Solution:
    def countSubIslands(sefl,grid1, grid2):
        rows = len(grid1)
        cols = len(grid1[0])

        def dfs(r,c):
            # outside grid or water -> nothing invalid here
            if (
                r < 0 or r >= rows
                or c < 0 or c >= cols
                or grid2[r][c] == 0
                ):
                return True
            
            #visited
            grid2[r][c] = 0

            # mask - cell must also be land in grid1
            is_sub_island = (grid1[r][c] == 1)

            # visit entire island even if one cell is invalid
            up = dfs(r-1,c)
            down = dfs(r+1, c)
            left = dfs(r, c-1)
            right = dfs(r,c+1)

            return ( is_sub_island and up and down and left and right)

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1:
                    if dfs(r,c):
                        count+=1

        return count

