from collections import deque

class Solution:
    def maximumMinutes(self, grid):
        m, n = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # multisource BFS - earliest time fire reaches cell
        fire_time = [[float('inf')]*n for _ in range(m)]
        q = deque()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fire_time[r][c] = 0
                    q.append((r,c))

        while q:
            r,c = q.popleft()

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                
                if (
                    0 <= nr < m
                    and 0 <= nc < n
                    and grid[nr][nc] != 2
                    and fire_time[nr][nc] == float('inf')
                ):
                    # not wall or not reached yet
                    fire_time[nr][nc] = fire_time[r][c] + 1
                    q.append((nr,nc))

        # can escape -> can we escape if we wait 'wait' minutes

        def can_escape(wait):
            # fire reaches start cell before/eq to departure
            if wait >= fire_time[0][0]: return False

            q = deque((0, 0, wait)) # r,c,wait
            visited = set([(0,0)])

            while q:
                r,c,t = q.popleft()
                for dr,dc in directions:
                    nr, nc = dr+r, dc+c
                    if (
                        nr < 0 or nr >= m
                        or nc < 0 or nc >= n
                        or grid[nr][nc] == 2
                        or (nr,nc) in visited
                        ):
                        continue
                    new_time = t + 1

                    # sepcial case - reach safehouse
                    if nr == m-1 and nc == n-1:
                        if new_time <= fire_time[nr][nc]:
                            return True
                        continue

                    # everywhere else - we must arrive before fire
                    if new_time < fire_time[nr][nc]:
                        visited.add((nr,nc))
                        q.append((nr,nc,new_time))

            return False

        # cant escape without waiting
        if not can_escape(0):
            return -1

        if can_escape(10**9):
            return 10**9

        # binary search to get max valid wait
        l,r = 0, 10**9
        while l <= r:
            m = (l+r)//2
            if can_escape(m):
                l = m+1
            else:
                r = m-1

        return True

