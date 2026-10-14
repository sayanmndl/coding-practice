class LooseMedian:
    def __init__(self):
        self.counts = [0]*64
        self.n = 0

    def insert(self, x):
        if x <= 0:
            raise ValueError

        bucket = x.bit_length() - 1
        self.count[bucket] += 1
        self.n += 1
    
    def looseMedian(self):
        if self.n == 0:
            raise ValueError

        target = (self.n + 1)//2 # lower rank, 1 indexed
        count = 0
        for bucket, freq in enumerate(self.counts):
            count += freq
            if count >= target:
                return 1 << bucket