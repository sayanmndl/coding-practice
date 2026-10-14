import heapq

class Solution:
    def minInterval(self, intervals, queries):
        intervals.sort()

        sorted_queries = sorted(
            (q,i) for i, q in enumerate(queries)
        )

        ans = [-1]*len(queries)

        min_heap =[]
        i = 0
        for q, original_idx in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= q:
                left, right = intervals[i]
                size = right - left + 1
                heapq.heappush(min_heap, (size, right))
                i+=1
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            
            # smallest valid interval
            if min_heap:
                ans[original_idx] = min_heap[0][0]
        return ans