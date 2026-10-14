

def mincostpoints(points):
    n = len(points)
    visited = set()
    min_dist = [float('inf')]*n

    min_dist[0] = 0
    total_cost = 0

    for _ in range(n):
        curr = -1
        for i in range(n):
            if i not in visited and (curr == -1 or min_dist[i] < min_dist[curr]):
                curr = i

        visited.add(curr)
        total_cost += min_dist[curr]

        x1,y1 = points[curr]
        for j in range(n):
            if j not in visited:
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                min_dist[j] = min(dist, min_dist[j])
    return total_cost


from collections import defaultdict
import heapq

def mincostpoints(points):
    n = len(points)
    visited = set()
    minheap = [(0,0)]
    total_cost = 0

    while minheap and len(visited) < n:
        cost, node = heapq.heappop(minheap)

        if node in visited:
            continue

        visited.add(node)
        total_cost+= cost
        x1,y1 = points[node]
        for neigh in range(n):
            if neigh not in visited:
                x2,y2 = points[neigh]
                w = abs(x1-x2)+abs(y1-y2)
                heapq.heappush(minheap, (w, neigh))
    return total_cost

def itinerary(tickets):
    graph = defaultdict(list)
    for u,v in tickets:
        heapq.heappush(graph[u], v)
    routes  = []
    def dfs(apt):
        while graph[apt]:
            nxt_apt = heapq.heappop(graph[apt])
            dfs(nxt_apt)
        routes.append(apt)
    dfs('JFK')
    return routes[::-1]