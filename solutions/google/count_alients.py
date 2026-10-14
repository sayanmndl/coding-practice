class Solution:
    def countAlienPairs(self, n, pairs):
        parent = list(range(n))
        size = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a,b):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return

            # union by size
            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a

            parent[root_b] = root_a
            size[root_a] += size[root_b]

        for a,b in pairs:
            union(a,b)

        planet_sizes = []

        for alien in range(n):
            if find(alien) == alien:
                planet_sizes.append(size[alien])

        result = 0
        remaining = n
        for group_size in planet_sizes:
            remaining -= group_size
            result += group_size * remaining

        return result