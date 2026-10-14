



class TrieNode:
    def __init__(self):
        self.children = {}
        self.param_child = None # represents {param}
        self.pattern = None # original registered pattern if route ends

class Router:
    def __init__(self):
        self.root = TrieNode()

    def _split(self, path):
        return [part for part in path.split('/') if part]

    def registerHandler(self, pattern):
        parts = self._split(pattern)
        node = self.root

        for part in parts:
            if part.startswith('{') and part.endswith('}'):
                if node.param_child is None:
                    node.param_child = TrieNode()
                node = node.param_child
            else:
                if part not in node.children:
                    node.children[part] = TrieNode()
                node = node.children[part]

        node.pattern = pattern

    def getHandler(self, path):
        parts = self._split(path)
        return self._search(self.root, parts, 0)

    def _search(self, node, parts, i):
        if i == len(parts):
            return node.pattern
        part = parts[i]

        # exact match
        if part in node.children:
            result = self._search(
                node.children[part],
                parts,
                i+1
            )
            if result is not None:
                return result
        
        # param match
        if node.param_child is not None:
            result = self._search(
                node.param_child,
                parts,
                i+1
            )
            if result is not None:
                return result
        return None


router = Router()

router.registerHandler("/users")
router.registerHandler("/users/{id}")
router.registerHandler("/users/{id}/profile")
router.registerHandler("/users/settings")
router.registerHandler("/posts/{postId}")

print(router.getHandler("/users"))
print(router.getHandler("/users/123"))
print(router.getHandler("/users/123/profile"))
print(router.getHandler("/users/settings"))
print(router.getHandler("/posts/42"))
print(router.getHandler("/comments/10"))