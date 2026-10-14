from collections import deque

class Solution:
    def minKnightMoves(self, x, y):
        x,y = abs(x), abs(y)

        moves = [
            (-2, 1), (-1, 2),
            (1, 2), (2, 1),
            (2, -1), (1, -2),
            (-1, -2), (-2, -1)
        ]

        queue = deque([(0,0,0)])
        visited = set([(0,0)])

        while queue:
            curr_x, curr_y, steps = queue.popleft()

            if curr_x==x and curr_y==y:
                return steps

            for dx, dy in moves:
                nx = curr_x+dx
                ny = curr_y+dy
                
                if nx >= -2 and ny >= -2 and (nx, ny) not in visited:
                    visited.add((nx,ny))
                    queue.append((nx,ny, steps+1))