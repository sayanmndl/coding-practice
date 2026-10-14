



class Solution:
    def trap(self, height):
        l, r = 0, len(height) - 1
        left_max = right_max = 0
        water = 0

        while l < r:
            if height[l] <= height[r]:
                if height[l] < left_max:
                    water += left_max - height[l]
                else:
                    left_max = height[l]
                l+=1
            else:
                if height[r] > right_max:
                    right_max = height[r]
                else:
                    water += right_max - height[r]
                r-=1
        return water
