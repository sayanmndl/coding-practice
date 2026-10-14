class Node:
    def __init__(self, name = "", path="/"):
        self.name = name
        self.path = path

        self.children = {}
        
        self.is_file = False
        self.file_size = 0

        # sum of all descendant files
        self.total_size = 0

        # sum of files directly inside this dir
        self.immediate_file_size = 0


class FileSystemAnalyzer:
    def __init__(self, files):
        self.root = Node()

        for path, size in files:
            self._insert_file(path, size)

        self._compute_total_size(self.root)

    # build tree
    def _inser_file(self, path, size):
        parts = path.strip('/').split('/')

        node = self.root
        current_path = ""

        for i, part in enumerate(parts):
            current_path += "/" + part

            if part not in node.children:
                node.children[part] = Node(
                    name=part, path = current_path
                )

            node = node.children[part]

        # last node is file
        node.is_file = True
        node.file_size = size

    # precompute recursive sizes
    def _compute_total_size(self, node: Node):
        if node.is_file:
            node.total_size = node.file_size
            return node.file_size
        
        total = 0
        immediate = 0

        for child in node.children.values():
            total += self._compute_total_size(child)

            if child.is_file:
                immediate += child.file_size

        node.total_size = total
        node.immediate_file_size = immediate

    # locate path
    def _find(self, path):
        if path == '/':
            return self.root

        node = self.root

        for part in path.strip('/').split('/'):
            if part not in node.children:
                return None
            node = node.children[part]
        return node

    # get size
    def getSize(self, path):
        node = self._find(path)

        if node is None: return -1

        if node.is_file: return node.file_size
    
        return node.total_size

    # quick select
    def _quickselect(self, arr, k):
        '''
        rearrange arr so that k largest by arr[i][1] occupy [0:k] 
        '''
        if k >= len(arr):
            return

        target = k - 1

        def partition(left, right):
            pivot = arr[right][1]
            i = left
            for j in range(left, right):
                if arr[j][1] > pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i+=1
            
            arr[i], arr[right] = arr[right], arr[i]
            return i

        left = 0
        right = len(arr) - 1

        while left <= right:
            pivot_index = partition(left, right)
            if pivot_index == target:
                return

            elif pivot_index < target:
                left = pivot_index+1
            else:
                right = pivot_index-1

    # largest files
    def largestFiles(self, directory, k):
        start = self._find(directory)

        if start is None or start.is_file:
            return []
        
        files = []

        def dfs(node:Node):
            for child in node.children.values():
                if child.is_file:
                    files.append([child.path, child.file_size])
                else:
                    dfs(child)

        dfs(start)

        if not files: return []

        k = min(k, len(files))

        self._quickselect(files, k)
        result = files[:k]

        result.sort(key= lambda x: x[1], reverse = True)
        return result

    # largest folder
    def largestFolders(self, directory, k):
        start = self._find(directory)

        if start is None or start.is_file:
            return []

        folders = []

        def dfs(node):
            folders.append([node.path. node.immediate_file_size])

            for child in node.children.values():
                if not child.is_file:
                    dfs(child)

        dfs(start)

        k = min(k, len(folders))
        self._quickselect(folders, k)
        result = folders[:k]
        result.sort(key=lambda x: x[1], reverse = True)
        return result
