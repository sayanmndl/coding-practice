class FileNode:
    def __init__(self):
        self.children = {}
        self.is_file = False
        self.content = ""

class FileSystem:
    def __init__(self):
        self.root = FileNode()

    def _get_parts(self, path):
        return [part for part in path.split("/") if part]

    def _traverse(self, path, create = False):
        node = self.root

        for part in self._get_parts(path):
            if part not in self.children:
                if not create:
                    return None
                node.children[part] = FileNode()
            
            node = node.children[part]
        
        return node


    def mkdir(self, path):
        self._traverse(path, create=True)

    def ls(self, path):
        node = self._traverse(path)

        if node.is_file:
            return [self._get_parts(path)[-1]]
        
        return sorted(node.children.keys())

    def addContentToFile(self, filePath, content):
        node = self._traverse(filePath, create=True)
        node.is_file = True
        node.content += content

    def readContentFromFile(self, filePath):
        node = self._traverse(filePath)
        return node.content
