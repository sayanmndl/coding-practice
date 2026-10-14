from collections import deque

def can_reach(routers, start, target, wireless_range):

    def within_range(a,b):
        x1, y1 = routers[a]
        x2, y2 = routers[b]

        return (x1 - x2) ** 2 + (y1-y2)**2 <= wireless_range ** 2

    queue = deque([start])
    visited = {start}

    while queue:
        curr = queue.popleft()
        if curr == target:
            return True
        for neigh in routers:
            if neigh not in visited and within_range(curr, neigh):
                visited.add(neigh)
                queue.append(neigh)
    return False