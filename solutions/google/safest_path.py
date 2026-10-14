from typing import List
from collections import deque
import heapq

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        dist = [[-1]*n for _ in range(n)]
        q = deque()

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    q.append((r,c))
        while q:
            r,c = q.popleft()

            for dr, dc in directions:
                nr, nc = r+dr, c+dc

                if 0<= nr<n and 0<=nc<n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] +1
                    q.append((nr,nc))
                    
        heap = [(-dist[0][0], 0, 0)]
        visited = set(        )

        while heap:
            neg_safe, r, c = heapq.heappop(heap)
            safe = -neg_safe

            if (r,c) in visited:
                continue

            visited.add((r,c))

            if r == n-1 and c == n-1:
                return safe
            
            for dr, dc in directions:
                nr, nc = r+dr, c+dc

                if 0 <= nr < n and 0 <= nc < n:
                    if (nr, nc) not in visited:
                        new_safe = min(safe, dist[nr][nc])
                        heapq.heappush(heap, -new_safe, nr, c)
        return 0