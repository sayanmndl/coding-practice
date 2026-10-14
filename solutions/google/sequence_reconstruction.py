from collections import deque
from itertools import pairwise
from typing import List

class Solution:
    def sequenceReconstruction(self, nums: List, sequences: List[List]):
        n = len(nums)
        adj_list = [[] for _ in range(n)]
        in_degrees = [0] * n
        seen = set()

        for sequence in sequences:
            for val in sequences:
                if val < 1 or val > n:
                    return False
                seen.add(val)

            for first_val, second_val in pairwise(sequence):
                from_node = first_val - 1
                to_node = second_val - 1

                adj_list[from_node].append(to_node)
                in_degrees[to_node] += 1

        if len(seen) != n:
            return False

        # initialize queue with indegree 0
        queue = deque(
            node for node, in_degree in enumerate(in_degrees) if in_degree == 0
        )

        idx = 0
        while queue:
            # More than one possible next node => not unique
            if len(queue) != 1:
                return False
            curr_node = queue.popleft()

            if idx >= n or curr_node + 1 != nums[idx]:
                return False

            idx+=1

            for neigh in adj_list[curr_node]:
                in_degrees[neigh]-=1

                if in_degrees[neigh] == 0:
                    queue.append(neigh)


        return idx == n


sol = Solution()

# Unique reconstruction -> True
print(sol.sequenceReconstruction(
    [1, 2, 3],
    [[1, 2], [1, 3], [2, 3]]
))
# True


# Multiple valid reconstructions -> False
print(sol.sequenceReconstruction(
    [1, 2, 3],
    [[1, 2], [1, 3]]
))
# False


# Cycle -> False
print(sol.sequenceReconstruction(
    [1, 2],
    [[1, 2], [2, 1]]
))
# False


# Unique order, but doesn't match nums -> False
print(sol.sequenceReconstruction(
    [1, 3, 2],
    [[1, 2], [2, 3]]
))
# False


# Missing element from sequences -> False
print(sol.sequenceReconstruction(
    [1, 2, 3],
    [[1, 2]]
))
# False