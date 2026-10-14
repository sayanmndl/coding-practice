class Solution:
    def longestIncreasingPath(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        memo = {}
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r,c)]
            best = 1
            for dr, dc in directions:
                nr, nc = r+dr, c+ dc

                if (0<=nr<rows and 0<=nc<cols and matrix[nr][nc] > matrix[r][c]):
                    best = max(best, 1+dfs(nr,nc))
            memo[(r,c)] = best
            return best

        answer = 0

        for r in range(rows):
            for c in range(cols):
                answer = max(answer, dfs(r,c))

        return answer