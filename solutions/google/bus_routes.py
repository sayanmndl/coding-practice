from collections import defaultdict, deque
from typing import List

class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:

        if source == target:
            return 0

        stop_to_buses = defaultdict(list)
        for bus, stops in enumerate(routes):
            for stop in stops:
                stop_to_buses[stop].append(bus)

        q = deque([(source, 0)])
        visited_stops = {source}
        visited_buses = set()

        while q:
            stop, count = q.popleft()

            for bus in stop_to_buses[stop]:
                if bus in visited_buses:
                    continue

                visited_buses.add(bus)

                for next_stop in routes[bus]:
                    if next_stop == target:
                        return count+1
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        q.append((next_stop, count+1))
        return -1