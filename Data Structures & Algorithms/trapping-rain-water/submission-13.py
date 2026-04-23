class Solution:
    def trap(self, height: List[int]) -> int:
        # each place can hold min(left_max, right_max) - height
        # can precompute this which takes O(n) time and space
        # can do this on the fly, taking O(1) space and O(n) time

        l, r = 0, len(height) - 1
        water = 0
        left_max, right_max = 0, 0

        while l <= r:
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])

            if left_max >= right_max:
                water += max(0, right_max - height[r])
                r -= 1
            else:
                water += max(0, left_max - height[l])
                l += 1
        
        return water