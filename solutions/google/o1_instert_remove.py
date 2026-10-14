import random

class RandomArray:
    def __init__(self):
        self.arr = []

    def insert(self, val):
        self.arr.append(val)

    def remove(self, idx):
        if idx < 0 or idx >= len(self.arr):
            raise IndexError('Index out of range')
        
        removed = self.arr[idx]

        self.arr[idx] = self.arr[-1]
        self.arr.pop()

        return removed

    def getRandom(self):
        if not self.arr:
            raise IndexError('Empty date structure')

        idx = random.randrange(len(self.arr))
        return self.arr[idx]


ds = RandomArray()

ds.insert(10)
ds.insert(20)
ds.insert(30)
ds.insert(40)
print(ds.arr)
# [10, 20, 30, 40]

ds.remove(1)
print(ds.arr)