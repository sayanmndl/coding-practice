class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = set()

        def dfs(city):
            visited.add(city)

            for neigh in range(n):
                if isConnected[city][neigh] == 1 and neigh not in visited:
                    dfs(neigh)
        provinces = 0
        for city in range(n):
            if city not in visited:
                provinces += 1
                dfs(city)
        return provinces