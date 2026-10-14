class CustomStack:
    def __init__(self, maxSize):
        self.max_size = maxSize
        self.stack = []
        self.inc = []

    def push(self, x):
        if len(self.stack) == self.max_size:
            return

        self.stack.append(x)
        self.inc.append(0)
    
    def pop(self):
        if not self.stack:
            return -1

        i = len(self.stack) - 1
        add = self.inc[i]

        if i > 0:
            self.inc[i-1] += add
        self.inc.pop()
        return self.stack.pop() + add

    def increment(self, k, val):
        if not self.stack:
            return

        i = min(k, len(self.stack)) - 1
        self.inc[i] += val