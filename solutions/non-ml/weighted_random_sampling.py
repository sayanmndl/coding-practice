# Problem 1 — Weighted Random Sampling
import random
import bisect

class WeightedSampler:
    def __init__(self, weights):
        if not weights:
            raise ValueError("Weights cannot be empty")
        
        if any(w < 0 for w in weights):
            raise ValueError("Weights cannot be negative")
        
        self.prefix = []

        total = 0
        for w in weights:
            total+=w
            self.prefix.append(total)
        
        if total == 0:
            raise ValueError("Weights cannot be zero")
        
        self.total = total

    def sample(self, manual =False):
        r = random.random() * self.total
        # bisect right: because we are picking from [low, high) (excluding high)
        if not manual:
            return bisect.bisect_right(self.prefix, r) # eg: prefix: [1,4,10], r = 3.2 -> bisect_right=1
        else:
            l,r = 0, len(self.prefix) - 1

            while l < r:
                m = (l+r)//2

                if r < self.prefix[m]:
                    r = m
                else:
                    l = m+1
            return l


