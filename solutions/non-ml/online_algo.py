
class OnlineMean:
    def __init__(self):
        self.count = 0
        self.mean = 0.0

    def update(self, x):
        self.count += 1

        self.mean += (x - self.mean) / self.count

        return self.mean

class OnlineVariance:
    def __init__(self):
        self.count = 0
        self.mean = 0.0
        self.M2 = 0.0

    def update(self, x):
        self.count += 1

        delta = x - self.mean
        self.mean += delta / self.count
        delta2 = x - self.mean

        self.M2 += delta * delta2

    def population_variance(self):
        if self.count == 0:
            return float("nan")
        return self.M2 / self.count

    def sample_variance(self):
        if self.count < 2:
            return float("nan")
        return self.M2 / (self.count - 1)