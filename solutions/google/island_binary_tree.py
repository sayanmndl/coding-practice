from collections import defaultdict

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def analyzeIslands(self, root):
        if not root:
            return {
                "total_islands": 0,
                "by_value": {},
                "sizes": []
            }

        island_count = 0
        by_value = defaultdict(int)
        sizes = []

        def dfs(node, parent_value):
            nonlocal island_count

            if not node:
                return 0

            # new island starts if:
            # - this is a root
            # value differs from parent
            is_new_island = (
                parent_value is None or node.val != parent_value
            )

            if is_new_island:
                island_count += 1
                by_value[node.val] += 1

                size = count_same_value(node, node.val)
                sizes.append((node.val, size))
            
            dfs(node.left, node.val)
            dfs(node.right, node.val)

        def count_same_value(node, value):
            if not node or node.val != value:
                return 0

            return (1+count_same_value(node.left, value)+count_same_value(node.right, value))

        dfs(root, None)

        return {
            "total_islands": island_count,
            "by_value": dict(by_value),
            "sizes": sizes
        }