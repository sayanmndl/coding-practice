
class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = None
    
class FileSystem:
    def __init__(self):
        self.root = TrieNode()

    def createPath(self,path, value):
        parts = path.split('/')[1:]
        node = self.root

        for part in parts[:-1]:
            if part not in node.children:
                return False
            node = node.children[part]
        
        last = parts[-1]

        if last in node.children:
            return False

        new_node = TrieNode()
        new_node.value = value
        node.children[last] = new_node
        return True

    def get(self, path):
        parts = path.split('/')[1:]
        node = self.root
        for part in parts:
            if part not in  node.children:
                return -1

            node = node.children[part]
        return node.value