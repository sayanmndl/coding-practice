import heapq

class Solution:
    def maxMinimumPath(self, grid):
        m,n = len(grid), len(grid[0])
        # heapq is min heap
        max_heap = [(-grid[0][0], 0, 0)]
        visited = set()

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while max_heap:
            neg_score, row, col = heapq.heappop(max_heap)
            score = - neg_score

            # reached destination
            if row == m-1 and col == n-1:
                return score

            if (row,col) in visited:
                continue

            visited.add((row,col))

            for dr, dc in directions:
                nr = dr + row
                nc = dc + col

                if (0 <= nr < m and 0<= nc < n and (nr,nc) not in visited):
                    new_score = min(score, grid[nr][nc])

                    heapq.heappush(max_heap,(-new_score, nr, nc))

        return -1
