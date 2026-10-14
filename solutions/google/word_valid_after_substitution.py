class Solution:
    def isValid(self, s):
        stack = []
        for char in s:
            if char == 'c':
                if len(stack)>=2 and stack[-1] == 'b' and stack[-2]=='a':
                    stack.pop()
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0