import heapq
from collections import Counter

def top_k_frequent(nums, k):
    freq_map = Counter(nums)

    min_heap = []

    for num, freq in freq_map.items():
        if len(min_heap) < k:
            heapq.heappush(min_heap, (freq, num))
        # if curr freq < min freq in the min heap
        elif freq > min_heap[0][0]:
            heapq.heapreplace(min_heap, (freq, num))

    result = [num for _, num in min_heap]
    return result

    

