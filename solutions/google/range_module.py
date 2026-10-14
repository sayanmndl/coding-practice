from typing import List

class RangeModule:
    def __init__(self):
        self.ranges = []

    def addRange(self, left: int, right: int):
        new_ranges = []
        placed = False

        for start, end in self.ranges:

            # curr interval is completely before new interval
            if end < left:
                new_ranges.append([start, end])

            # curr interval is afte new interval
            elif right < start:
                if not placed:
                    new_ranges.append([left, right])
                    placed = True
                
                new_ranges.append([start, end])
            
            # overlap
            else:
                left = min(left, start)
                right = max(right, end)

        if not placed:
            new_ranges.append([left, right])
        
        self.ranges = new_ranges

    
    def queryRanges(self, left: int, right: int):
        for start, end in self.ranges:
            if start <= left and right <= end:
                return True

            if start > left:
                return False
        return False

    def removeRanges(self, left, right):
        new_ranges = []
        for start, end in self.ranges:
            # no overlap
            if end <= left or start >= right:
                new_ranges.append([start, end])
            
            if start < left:
                new_ranges.append([start, left])
            
            if end > right:
                new_ranges.append([right, end])
        self.ranges = new_ranges

    
rm = RangeModule()

rm.addRange(10, 20)
rm.addRange(15, 25)

print(rm.ranges)
# [[10, 25]]

print(rm.queryRange(12, 18))
# True

rm.removeRange(14, 17)

print(rm.ranges)
# [[10, 14], [17, 25]]

print(rm.queryRange(13, 18))
# False