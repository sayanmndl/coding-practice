
from turtle import end_fill


def employeeFreeTime(schedule):
    intervals = []

    for employee in schedule:
        for start, end in employee:
            intervals.append([start, end])

    intervals.sort(key=lambda x: x[0])

    result = []
    current_end = intervals[0][1]

    for start, end in intervals[1:]:
        if start > current_end:
            result.append([current_end, start])
        current_end = max(current_end, end)

    return result

def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: x[1])
    removals  = 0
    prev_end = float('-inf')

    for start, end in intervals:
        if start >= prev_end:
            prev_end = end
        else:
            removals +=1
    return removals