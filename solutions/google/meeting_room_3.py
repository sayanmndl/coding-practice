import heapq

class Solution:
    def mostBooked(self, n, meetings):
        meetings.sort()

        # free rooms: always choose smallest room number
        available = list(range(n))
        heapq.heapify(available)

        busy = []
        count = [0]*n # number or meetings

        for start, end in meetings:
            duration = end - start
            while busy and busy[0][0] <= start:
                end_time, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            if available:
                room = heapq.heappop(available)
                new_end = end
            else:
                # no room available
                earliest_end, room = heapq.heappop(busy)
                new_end = earliest_end + duration
            count[room]+=1
            heapq.heappush(busy, (new_end, room))
        return max(range(n), key = lambda x: (count[room], -room))