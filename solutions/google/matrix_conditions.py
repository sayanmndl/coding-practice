from collections import defaultdict, deque


class Solution:
    def buildMatrix(self, k, rowConditions, colConditions):
        
        def topo_sort(conditions):
            graph = defaultdict(list)
            indegree = [0]*(k+1)

            for u,v in conditions:
                graph[u].append(v)
                indegree[v]+=1
            
            queue = deque()
            for node in range(1, k+1):
                if indegree[node] == 0:
                    queue.append(node)
                
            order = []
            while queue:
                node = queue.popleft()
                order.append(node)

                for neigh in graph[node]:
                    indegree[neigh]-=1
                    if indegree[neigh]==0:
                        queue.append(neigh)
            # cycle
            if len(order) != k:
                return []
            
            return order

        row_order = topo_sort(rowConditions)
        col_order = topo_sort(colConditions)

        if not row_order or not col_order:
            return []

        row_pos = {value: i for i, value in enumerate(row_order)}
        col_pos = {value:i for i, value in enumerate(col_order)}
        matrix = [[0]*k for _ in range(k)]
        for value in range(1,k+1):
            r = row_pos[value]
            c = col_pos[value]
            matrix[r][c] = value
        return matrix