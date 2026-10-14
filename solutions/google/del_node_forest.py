from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List):
        delete = set(to_delete)
        forest = []

        def dfs(node, is_root):
            if not node:
                return None

            deleted = node.val in delete

            # If parent was deleted, this node becomes a new root
            if is_root and not deleted:
                forest.append(node)

            # Children become roots if current node is deleted
            node.left = dfs(node.left, deleted)
            node.right = dfs(node.right, deleted)

            return None if deleted else node

        dfs(root, True)
        return forest



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

solution = Solution()
forest = solution.delNodes(root, [3, 5])

print("Forest roots:")
for tree in forest:
    print(tree.val)