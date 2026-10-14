class Codec:

    def serialize(self, root):
        res = []

        def dfs(node):
            if not node:
                res.append('N')
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return ','.join(res)

    def deserialize(self, data):
        vals = iter(data.split(','))

        def dfs():
            val = next(vals)
            if val == 'N':
                return None

            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()