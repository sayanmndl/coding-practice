from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        INF = float("inf")
        dist = [INF] * n
        dist[src] = 0

        for _ in range(k+1):
            temp = dist.copy()

            for u, v, price in flights:
                if dist[u] == INF:
                    continue
                temp[v] =min(temp[v], dist[u]+price)
            dist = temp

        return -1 if dist[dst] == INF else dist[dst]


    def findCheapestPrice(
        self,
        n: int,
        flights,
        src: int,
        dst: int,
        k: int
    ) -> int:

        graph = defaultdict(list)

        for u, v, price in flights:
            graph[u].append((v, price))

        # (cost, node, flights_used)
        min_heap = [(0, src, 0)]

        # Cheapest cost to reach node using exactly x flights
        best = {}

        while min_heap:
            cost, node, flights_used = heapq.heappop(min_heap)

            # Since heap is ordered by cost, first valid dst is cheapest
            if node == dst:
                return cost

            # k stops => at most k + 1 flights
            if flights_used == k + 1:
                continue

            state = (node, flights_used)

            if state in best and best[state] < cost:
                continue

            for nei, price in graph[node]:
                new_cost = cost + price
                new_flights = flights_used + 1

                state = (nei, new_flights)

                if state not in best or new_cost < best[state]:
                    best[state] = new_cost

                    heapq.heappush(
                        min_heap,
                        (new_cost, nei, new_flights)
                    )

        return -1