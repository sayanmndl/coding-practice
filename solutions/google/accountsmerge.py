from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts):
        parent = {}
        rank = {}
        email_to_name = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a,b):
            rank_a = find(a)
            rank_b = find(b)

            if rank_a == rank_b:
                return

            if rank[rank_a] < rank[rank_b]:
                parent[rank_a] = rank_b
            elif rank[rank_a] > rank[rank_b]:
                parent[rank_b] = rank_a
            else:
                parent[rank_b] = rank_a
                rank[rank_a] += 1

        for account in accounts:
            name = account[0]
            first_email = account[1]

            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                    rank[email] = 0
                email_to_name[email] = name
                union(first_email, email)
        groups = defaultdict(list)
        for email in parent:
            root = find(email)
            groups[root].append(email)

        result = []

        for root, emails in groups.items():
            name = email_to_name[root]
            result.append([name] + sorted(emails))
        return result