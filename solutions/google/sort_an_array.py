from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        def heapify(i,size):
            while True:
                largest = i
                left = 2*i+1
                right = 2*i+2

                if left < size and nums[left] > nums[largest]:
                    largest = left
                if right < size and nums[right] > nums[largest]:
                    largest = right
                if largest == i:
                    break

                nums[i], nums[largest] = nums[largest], nums[i]
                i = largest
        
        for i in range(n//2 -1, -1, -1):
            heapify(i, n)

        for end in range(n-1, 0, -1):
            nums[0], nums[end] = nums[end], nums[0]
            heapify(0, end)

        return nums