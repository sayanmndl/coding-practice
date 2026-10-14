

class MyCalender:
    def __init__(self):
        self.bookings = []

    def book(self, startTime, endTime):
        for start, end in self.bookings:
            if startTime < end and endTime > start:
                return False

        self.bookings.append((startTime, endTime))
        return True