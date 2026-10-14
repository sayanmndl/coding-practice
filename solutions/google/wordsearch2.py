class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board, words):
        root = TrieNode()

        # build tree
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]

            node.word = word
        
        rows = len(board)
        cols = len(board[0])
        result = []

        def dfs(r, c, node):
            char = board[r][c]

            # current path is not a prefix of any word
            if char not in node.children:
                return

            next_node = node.children[char]

            # found a complete word
            if next_node.word is not None:
                result.append(next_node.word)

                next_node.word = None # prevent duplicates
            
            # mark cell as visited
            board[r][c] = '#'

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr = r + dr
                nc = c + dc
                if (
                    0<=nr<rows
                    and 0<=nc<cols
                    and board[nr][nc] != "#"
                    ):
                    dfs(nr,nc, next_node)
            # backtrack
            board[r][c] = char

        # start dfs from every cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        
        return result