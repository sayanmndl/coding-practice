import random

class RandomizedSet:
    def __ini__(self):
        self.values = [] # values[i] = elements stored at index i
        self.pos = {} # pos[val] = index of val in values

    def insert(self, val: int):
        if val in self.values:
            return False
        
        self.pos[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val):
        if val not in self.pos:
            return False

        idx = self.pos[val]

        # move last element to idx so we dont need o(n) deletion
        last = self.values[-1]
        self.values[idx] = last
        self.pos[last] = idx

        self.values.pop()
        del self.pos[val]

        return True

    def getRandom(self):
        return random.choice(self.values)