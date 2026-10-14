from collections import deque

class Solution:
    def minPushBox(self, grid):
        m,n = len(grid), len(grid[0])

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 'S':
                    player = (r,c)
                elif grid[r][c] == 'B':
                    box = (r,c)
                elif grid[r][c] == 'T':
                    target = (r,c)

        directions = [
            (1,0), (-1,0), (0,1), (0,-1)
        ]

        def valid(r,c):
            return (
                0<=r<m
                and 0<=c<n
                and grid[r][c] != '#'
            )
        
        # can player walk from start -> target
        def can_reach(start, target_cell, box_pos):
            if start == target_cell:
                return True
            
            q = deque([start])
            visited = {start}

            while q:
                r,c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    nxt = (nr,nc)

                    if (
                        valid(nr,nc)
                        and nxt != box_pos
                        and nxt not in visited
                        ):
                        if nxt == target_cell:
                            return True
                        
                        visited.add(nxt)
                        q.append(nxt)
            return False

        # start = (box_pos, player_pos, pushes)
        q = deque([(box,player,0)])
        visited = {(box,player)}

        while q:
            box_pos, player_pos, pushes = q.popleft()
            if box_pos == target:
                return pushes

            br, bc = box_pos
            for dr, dc in directions:
                new_box = (br+dr, bc+dc)
                required_player = (br - dr, bc - dc)

                if not valid(*new_box):
                    continue
                if not valid(*required_player):
                    continue

                if not can_reach(
                    player_pos, required_player, box_pos
                    ):
                    continue

                new_player = box_pos
                state = (new_box, new_player)
                if state not in visited:
                    visited.add(state)
                    q.append((new_box, new_player, pushes + 1))

        return -1