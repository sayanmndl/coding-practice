import heapq
from operator import neg

class StockPrice:

    def __init__(self):
        self.prices = {}
        self.latest = 0
        self.min_heap = []
        self.max_heap = []
        

    def update(self, timestamp: int, price: int) -> None:
        self.prices[timestamp] = price
        self.latest = max(self.latest, timestamp)

        heapq.heappush(self.min_heap, (price, timestamp))
        heapq.heappush(self.max_heap, (-price, timestamp))
        

    def current(self) -> int:
        return self.prices[self.latest]
        

    def maximum(self) -> int:
        while self.max_heap:
            neg_price, timestamp =self.max_heap[0]

            if self.prices[timestamp]==-neg_price:
                return -neg_price
            heapq.heappop(self.max_heap)
        

    def minimum(self) -> int:
        while self.min_heap:
            price, timestamp = self.min_heap[0]
            if self.prices[timestamp] == price:
                return price
            heapq.heappop(self.min_heap)
