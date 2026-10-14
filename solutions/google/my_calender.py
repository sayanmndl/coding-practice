
class MyCalenderTwo:
    def __init__(self):
        self.bookings = []
        self.overlaps = []

    def book(self, startTime, endTime):
        for start, end in self.overlaps:
            if max(start, startTime) < min(end, endTime):
                return False

        for start, end in self.bookings:
            overlap_start = max(start, startTime)
            overlap_end = min(end, endTime)

            if overlap_start < overlap_end:
                self.overlaps.append([overlap_start, overlap_end])

        self.bookings.append([startTime, endTime])
        return True