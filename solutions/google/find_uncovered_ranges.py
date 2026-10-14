def find_uncovered_ranges(n, ranges):
    if n == 0:
        return []

    if not ranges:
        return [[0, n-1]]

    ranges.sort()
    uncovered = []
    current = 0 # first position not accounted for

    for start, end in ranges:
        if end < 0 or start >= n:
            continue

        start = max(start, 0)
        end = min(end, n-1)

        if current < start:
            uncovered.append([current, start - 1])

        current = max(current, end+1)

        if current >= n:
            break
    if current < n:
        uncovered.append([current, n-1])

    return uncovered