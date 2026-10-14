import random
from typing import List

class Solution:
    def __init__(self, n, blacklist):
        self.m = n - len(blacklist)
        black  = set(blacklist)

        # Only blacklisted numbers in [0, m-1] need to be remaped
        self.mapping = {}
        w = self.m # valid numbers from upper range [m,n-1]
        for b in blacklist:
            if b < self.m:
                while w in black:
                    w+=1
                
                self.mapping[b] = w
                w+=1

    def pick(self):
        x = random.randrange(self.m)
        return self.mapping.get(x,x)
