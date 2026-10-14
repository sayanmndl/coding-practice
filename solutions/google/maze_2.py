import heapq

class Solution:
    def shortedtDistance(self, maze, start, destination):
        m,n = len(maze), len(maze[0])

        dist = [[float('inf')] * n for _ in range(m)]
        sr,sc = start
        dr, dc = destination

        dist[sr][sc] = 0

        # (distance, row, col)
        min_heap = [(0, sr, sc)]

        directions = [
            (1,0), (-1,0), (0,1), (0,-1)
        ]

        while min_heap:
            curr_dist, r, c = heapq.heappop(min_heap)

            if curr_dist > dist[r][c]:
                continue

            if r == dr and c == dc:
                return curr_dist
            
            for row_dir, col_dir in directions:
                nr, nc = r, c
                steps = 0

                while (
                    0 <= nr + row_dir < m and 0 <= nc + col_dir < n
                    and maze[nr+row_dir][nc+col_dir] ==0
                    ):
                    nr += row_dir
                    nc += col_dir
                    steps += 1

                new_dist = curr_dist + steps

                if new_dist < dist[nr][nc]:
                    dist[nr][nc] = new_dist
                    heapq.heappush(min_heap, (new_dist, nr, nc))

        return -1