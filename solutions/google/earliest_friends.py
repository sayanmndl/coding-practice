class Solution:
    def earliestAcq(self, logs, n):
        parent = list(range(n))
        rank=[0]*n
        components = n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a,b):
            nonlocal components
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return False

            if rank[root_a] < rank[root_b]:
                root_a, root_b = root_b, root_a
            
            parent[root_b] = root_a

            # rank only increases when both ransk were equal
            if rank[root_a] == rank[root_b]:
                rank[root_a]+=1
            components-=1
            return True
        logs.sort()
        for timestamp, x, y in logs:
            union(x,y)
            if components == 1:
                return timestamp
        return -1