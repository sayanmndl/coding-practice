from collections import deque
from curses import nonl


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findLeaves(root):
    res = []

    def getHeight(node):
        if node is None:
            return -1

        letfHeight = getHeight(node.left)
        rightHeight = getHeight(node.right)

        currHeight = max(letfHeight, rightHeight) + 1

        if currHeight == len(res):
            res.append([]) # new height so new list
        res[currHeight].append(node.val)
    
        return currHeight
    
    getHeight(root)
    return res


def num_islands(grid):
    if not grid or not grid[0]:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    islands = 0

    dirs = [(-1,0), (0,-1), (0,1), (1,0)]

    def dfs(r,c):

        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return

        grid[r][c] = '0' #visited

        for dr, dc in dirs:
            dfs(r+dr, c+dc)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                islands += 1
                dfs(r,c)
    return islands


def depthSumInverse(nestedList):
    
    if not nestedList:
        return 0

    queue = deque(nestedList)
    total_sum = 0
    level_sum = 0

    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            element = queue.popleft()
            if isinstance(element, int):
                level_sum+= element
            else:
                for nested in element:
                    queue.append(nested)
        total_sum+=level_sum # add curr level sum to total (carries forward)
    return total_sum


def diameter(root):

    max_diameter = 0

    def dfs(node):
        if node is None:
            return 0
        max_depth_1 = 0 # longest path
        max_depth_2 = 0 # shortest path

        for child in node.children:
            child_depth = dfs(child)

            if child_depth > max_depth_1:
                max_depth_2 = max_depth_1
                max_depth_1 = child_depth
            elif child_depth > max_depth_2:
                max_depth_2 = child_depth
        
        nonlocal max_diameter
        max_diameter = max(max_diameter, max_depth_1+max_depth_2)

        return 1 + max_depth_1
    
    dfs(root)
    return max_diameter

def diameter_binary(root):
    max_diameter = 0

    def dfs(node):
        nonlocal max_diameter
        if node is None:
            return 0
        
        left_depth = dfs(node.left)
        right_depth = dfs(node.right)

        max_diameter = max(max_diameter, left_depth+right_depth)
        return 1 + max(left_depth, right_depth)

    dfs(root)
    return max_diameter