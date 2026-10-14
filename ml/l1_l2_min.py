
def best_l1_point(x):
    if not x:
        raise

    values = sorted(x)
    n = len(values)

    if n%2 ==1:
        return values[n//2]
    
    return (values[n//2 - 1] + values[n//2])/2


def best_l2_point(x):
    if not x:
        raise

    return sum(x)/len(x)

def l1_loss(x,c):
    return sum(abs(v-c) for v in x)

def l2_loss(x,c):
    return (sum((v-c)**2) for v in x)

import random

def quickselect(nums, k):
    if not 0 <= k < len(nums):
        raise ValueError("k out of range")

    left, right = 0, len(nums) - 1

    while True:
        pivot_idx = random.randint(left, right)
        pivot = nums[pivot_idx]

        # Move pivot to the end
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

        # Partition
        store = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[store], nums[i] = nums[i], nums[store]
                store += 1

        # Put pivot into its final sorted position
        nums[store], nums[right] = nums[right], nums[store]

        if store == k:
            return nums[store]
        elif k < store:
            right = store - 1
        else:
            left = store + 1