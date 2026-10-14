
def merge_intervals(intervals):
    if not intervals:
        return []
    
    intervals.sort(key= lambda x: x[0])

    merged = [intervals[0]]

    for _int in intervals[1:]:

        if _int[0] <= merged[-1][-1]:
            merged[-1][-1] = max(merged[-1][-1], _int[1])
        else:
            merged.append(_int)

    return merged


intervals = [[1,3], [2,6], [8,10], [15,18]]
print(merge_intervals(intervals))