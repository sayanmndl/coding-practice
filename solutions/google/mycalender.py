from collections import defaultdict

class MyCalenderThree:
    def __init__(self):
        self.delta = defaultdict(int)

    def book(self, startTime: int, endTime: int):
        self.delta[startTime] += 1
        self.delta[endTime]-=1

        active = 0
        max_booking = 0

        for time in sorted(self.delta):
            active+= self.delta[time]
            max_booking = max(max_booking, active)
        return max_booking