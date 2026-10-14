
class Solution:
    def carPooling(self, trips, capacity):
        max_location = max(end for _, _, end in trips)
        changes = [0] * (max_location + 1)

        for passengers, start, end in trips:
            changes[start] += passengers
            changes[end] -= passengers
        current = 0

        for change in changes:
            current += change
            if current > capacity:
                return False
        return True