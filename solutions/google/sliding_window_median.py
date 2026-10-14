from collections import defaultdict
import heapq
from unittest import result

class Solution:
    def medianSlidingWindoe(self, nums, k):
        small = []
        large = []
        delayed = defaultdict(int)

        small_size = 0
        large_size = 0

        def prune(heap):
            while heap:
                num = -heap[0] if heap is small else heap[0]

                if delayed[num] == 0:
                    break

                delayed[num] -= 1
                heapq.heappop(heap)

        def balance():
            nonlocal small_size,large_size

            if small_size > large_size+1:
                val = -heapq.heappop(small)
                heapq.heappush(large, val)

                small_size -= 1
                large_size += 1
                prune(small)

            elif small_size < large_size:
                val = heapq.heappop(large)
                heapq.heappush(small, -val)
                large_size -= 1
                small_size+=1
                prune(large)

        def add(num):
            nonlocal small_size, large_size

            if not small or num <= -small[0]:
                heapq.heappush(small, -num)
                small_size+=1
            else:
                heapq.heappush(large, num)
                large_size+=1
            balance()
        
        def remove(num):
            nonlocal small_size, large_size
            delayed[num] += 1

            if num <= -small[0]:
                small_size -=1

                if num == -small[0]:
                    prune(small)

            else:
                large_size -= 1

                if large and num == large[0]:
                    prune(large)
            balance()

        def get_median():
            if k%2 == 1:
                return float(-small[0])
            return (-small[0] + large[0]) / 2.0

        for i in range(k):
            add(nums[i])
        result = [get_median()]

        for i in range(k, len(nums)):
            add(nums[i])
            remove(nums[i-k])
            result.append(get_median())
        return result
