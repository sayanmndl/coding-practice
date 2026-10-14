from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(list)

        for (a,b), value in zip(equations, values):
            graph[a].append((b,value))
            graph[b].append((a, 1/value))

        def dfs(src, dst, visited):
            if src == dst:
                return 1.0

            visited.add(src)
            for neigh, weight in graph(src):
                if neigh in visited:
                    continue
                result = dfs(neigh, dst, visited)
                if result != -1.0:
                    return weight * result
            return -1.0

        answer = []

        for src, dst in queries:
            if src not in graph or dst not in graph:
                answer.append(-1.0)
                continue
            answer.append(dfs(src,dst,set()))
        return answer