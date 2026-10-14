from collections import defaultdict

class Solution:
    def subArraySum(self, nums, k):
        count = 0
        curr_sum = 0
        running_sum = defaultdict(int)
        running_sum[0] = 1

        for n in nums:
            curr_sum += n
            target = curr_sum - k

            if target in running_sum:
                count += running_sum[target]
            running_sum[curr_sum]+=1
        return count