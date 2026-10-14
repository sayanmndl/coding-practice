class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)

        visited = [False]*n
        min_dist = [float('inf')] * n

        min_dist[0] = 0
        total_cost = 0

        for _ in range(n):
            curr = -1
            for i in range(n):
                if not visited[i] and (curr == -1 or min_dist[i] < min_dist[curr]):
                    curr = i
                    
            visited[curr] = True
            total_cost += min_dist[curr]
            x1,y1 = points[curr]

            for next_node in range(n):
                if not visited[next_node]:
                    x2,y2 = points[next_node]
                    distance = abs(x1-x2) + abs(y1-y2)
                    min_dist[next_node] = min(min_dist[next_node], distance)
        return total_cost