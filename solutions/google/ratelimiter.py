from collections import deque
from threading import Lock

class RateLimiter:
    def __init__(self):
        self.rps = 0
        self.accepted = deque()
        self.lock = Lock()

    def Allowable(self, rps):
        with self.lock:
            self.rps = rps

    def Allow(self, reqTimestamp):
        with self.lock:
            while ( self.accepted and self.accepted[0] <= reqTimestamp - 1000 ):
                self.accepted.popleft()
            
            # Rate limit reached
            if len(self.accepted) >= self.rps:
                return False

            # accept request
            self.accepted.append(reqTimestamp)
            return True
