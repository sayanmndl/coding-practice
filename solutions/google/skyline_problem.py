import heapq

class Solution:
    def getSkyLine(self, buildings):
        events = []

        for left, right, height in buildings:
            events.append((left, -height, right))

        for _, right, _ in buildings:
            events.append((right, 0,0))
        
        events.sort()
        result = []
        heap = [(0, float('inf'))]
        prev_height = 0

        for x, neg_height, right in events:
            while heap[0][1] <= x:
                heapq.heappop(heap)
            
            if neg_height != 0:
                heapq.heappush(heap, (neg_height, right))
            curr_height = -heap[0][0]

            if curr_height != prev_height:
                result.append([x, curr_height])
                prev_height = curr_height
        return result