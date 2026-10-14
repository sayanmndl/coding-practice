class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0]*(4 * n)

    def constructTree(self, input_arr, seg_tree, low, high, pos):
        # pos = idx in arr
        if low == high:
            seg_tree[pos] = input_arr[low]
        
        mid = (low + high)//2

        self.constructTree(input_arr, seg_tree, low, mid, 2*pos+1) # one of the leaves in arr
        self.constructTree(input_arr, seg_tree, mid+1, high, 2*pos+2) # other leaf

        seg_tree[pos] = max(seg_tree[2*pos+1], seg_tree[2*pos+2])

    def rangeMaximumQuery(self, seg_tree, qlow, qhigh, low, high, pos):
        if qlow <= low and qhigh >= high: # total overlap
            return seg_tree[pos]

        if qlow > high or qhigh < low: # no overlap
            return 0

        # partial overlap
        mid = (low + high)//2

        return max(
            self.rangeMaximumQuery(seg_tree, qlow, qhigh, low, mid, 2*pos+1),
            self.rangeMaximumQuery(seg_tree, qlow, qhigh, mid+1, high, 2*pos+2) # check both leaves
        )

    def update(self, seg_tree, low, high, index, value, pos):
        if low == high:
            seg_tree[pos] = max(seg_tree[pos], value)
            return

        mid = (low + high)//2

        if index <= mid:
            self.update(seg_tree, low, mid, index, value, 2*pos+1)
        else:
            self.update(seg_tree, mid+1, high, index, value, 2*pos+2)
        
        seg_tree[pos] = max(
            seg_tree[2*pos+1],
            seg_tree[2*pos+2]
        )


class Solution:
     def lenghtofLIS(self, nums, k):
        max_value = max(nums)
        dp = [0]*(max_value+1)

        seg_tree = [0]*(4 * len(dp))
        tree = SegmentTree()

        answer = 0
        for x in nums:
            qlow = max(0, x-k)
            qhigh = x - 1

            best = 0
            if qlow <= qhigh:
                best = tree.rangeMaximumQuery(seg_tree, qlow, qhigh, 0, max_value, 0)

            current = best + 1
            tree.update(seg_tree, 0, max_value, x, current, 0)
            answer = max(answer, current)
        
        return answer
