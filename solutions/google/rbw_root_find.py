from collections import defaultdict

def find_binary_root(n, edges):
    graph = [[] for _ in range(n)]

    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)

    for node in range(n):
        if len(graph[node]) <= 2:
            return node

    return -1