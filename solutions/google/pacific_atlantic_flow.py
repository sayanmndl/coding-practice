


class Solution:
    def pacificAtlantic(self, heights):
        rows, cols = len(heights), len(heights[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r, c, visited):
            visited.add((r,c))

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if (
                    0<=nr<rows and 0<=nc<cols
                    and (nr,nc) not in visited
                    and heights[nr][nc] >= heights[r][c]
                    ):
                    dfs(nr,nc)
        pacific = set()
        atlantic = set()

        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows - 1, c, atlantic)

        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols-1, atlantic)
        
        result = []

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    result.append([r,c])
        return result