from collections import deque

def openLock(deadends, target):
    dead = set(deadends)

    if '0000' in dead:
        return -1

    queue = deque([('0000', 0)])
    visited = {'0000'}

    while queue:
        state, turns = queue.popleft()

        if state == target:
            return turns
        
        for i in range(4):
            digit = int(state[i])

            for change in (-1,1):
                new_digit = (digit + change) % 10
                neigh = (state[:i]+str[new_digit]+state[i+1:])

                if neigh not in dead and neigh not in visited:
                    visited.add(neigh)
                    queue.append((neigh, turns+1))
    return -1