class Node:
    def __init__(self, val = 0, neighs = None):
        self.val = val
        self.neighs  = neighs if neighs is not None else []

class Solution:
    def cloneGraph(self, node: 'Node'):
        if not node:
            return None

        clones = {}

        def dfs(curr):
            if curr in clones:
                return clones[curr]

            copy = Node(curr.val)
            clones[curr] = copy

            for neigh in curr.neighs:
                copy.neighs.append(dfs(neigh))
            return copy

        return dfs(node)