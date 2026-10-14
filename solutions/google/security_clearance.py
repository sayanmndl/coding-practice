import heapq
from collections import defaultdict

# minimax dijkstra

def min_security_clearance(n, edges, src, dst):
    graph = defaultdict(list)

    for u, v, security in edges:
        graph[u].append((v, security))

    # clearance[node] = min security level needed to reach node
    clearance = {node: float('inf') for node in range(1, n+1)}
    clearance[src] = 0

    # (req clearance, node)
    heap = [(0, src)]

    while heap:
        curr_clearance, node = heapq.heappop(heap)

        if node == dst:
            return curr_clearance

        if curr_clearance > clearance[node]:
            continue

        for neigh, security in graph[node]:
            new_clearance = max(curr_clearance, security)

            if new_clearance < clearance[neigh]:
                clearance[neigh] = new_clearance
                heapq.heappush(heap, (new_clearance, neigh))

    return -1

n = 4

edges = [
    (1, 2, 3),
    (1, 3, 2),
    (3, 4, 3),
    (2, 4, 5)
]

print(min_security_clearance(
    n, edges, 1, 4
))

# Security + Edge weights
# min security clearance + min total path cost

def shortest_path_min_security(n, edges, src, dst):
    graph = defaultdict(list)

    for u, v, security, cost in edges:
        graph[u].append((v, security, cost))

    # track node: (min security, min cost) to reach that node
    best = {
        node: (float('inf'), float('inf')) for node in range(1, n+1)
    }

    best[src] = (0,0)

    # (security needed, total cost, node)
    heap = [(0,0, src)]

    while heap:
        security, cost, node = heapq.heappop(heap)

        if (security, cost) != best[node]:
            continue

        if node == dst:
            return security, cost

        for neigh, curr_security, curr_cost in graph[node]:
            new_security = max(security, curr_security)
            new_cost = curr_cost + cost

            new_state = (new_security, new_cost)

            if new_state < best[neigh]:
                best[neigh] = new_state
                heapq.heappush(heap, (new_security, new_cost, neigh))
    return -1, -1 

n = 4

edges = [
    (1, 2, 3, 2),
    (1, 3, 2, 5),
    (3, 4, 3, 2),
    (2, 4, 5, 1)
]

clearance, distance = shortest_path_min_security(
    n, edges, 1, 4
)

print(clearance)
print(distance)