class Solution:
    def applyQueriesConstantK(self, nums, queries):
        n = len(nums)

        # parent[i] -> next unprocessed index >=i
        parent = list(range(n+1))

        def find(x):
            # return nxt unprocessed index >= x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        # process reverse betcause last write wins
        for L, R, K in reversed(queries):
            i = find[L]
            while i <= R:
                # final value for index i
                nums[i]=K
                # remove i from furtue consideration
                parent[i] = find(i+1)
                i = find[i]
        return nums

