import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)

        for u,v,w in times:
            graph[u].append((v,w))

        min_heap = [(0,k)] # time, node
        dist = {} # visited

        while min_heap:
            time, node = heapq.heappop(min_heap)

            if node in dist:
                continue

            for neigh, weight in graph[node]:
                if neigh not in dist:
                    heapq.heappush(min_heap, (time+weight, neigh))
        
        if len(dist) != n:
            return -1
        return max(dist.values())
