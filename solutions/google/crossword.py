class Solution:
    def placWordInCrossword(self, board, word):
        m,n = len(board), len(board[0])
        rev = word[::-1]

        def fits(slot):
            if len(slot) != len(word):
                return False

            def matches(candidate):
                for cell, ch in zip(slot, candidate):
                    if cell != ' ' and cell != ch:
                        return False
                return True
            return matches(word) or matches(rev)
        
        for r in range(m):
            start = 0
            for c in range(n+1):
                if c == n or board[r][c] == '#':
                    slot = board[r][start:c]
                    if fits(slot):
                        return True
                    start = c+1

        for c in range(n):
            start = 0
            for r in range(m+1):
                if r==m or board[r][c] == '#':
                    slot = [board[i][c] for i in range(start, r)]
                    if fits(slot):
                        return True
                    start = r + 1
        
        return False