import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        intervals.sort(key = lambda x: x[0])

        heap = []
        for start, end in intervals:
            if heap and start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
        return len(heap)