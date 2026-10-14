class Solution:
    def insert(self, intervals, newinterval):
        result = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newinterval[0]:
            result.append(intervals[i])
            i+=1

        while i < n and intervals[i][0] <= newinterval[1]:
            newinterval[0] = min(newinterval[0], intervals[i][0])
            newinterval[1] = max(newinterval[1], intervals[i][1])
            i+=1
        result.append(newinterval)

        while i < n:
            result.append(intervals[i])
        return result