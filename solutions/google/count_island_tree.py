class TrieNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def count_islands(root):
    if not root:
        return 0

    def dfs(node, parent_is_one):
        if not node:
            return 0

        islands = 0

        if node.val == 1 and not parent_is_one:
            islands+=1
        islands += dfs(node.left, node.val == 1)
        islands += dfs(node.right, node.val == 1)
        return islands
    
    return dfs(root, False)