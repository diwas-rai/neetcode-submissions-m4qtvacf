class Solution:
    def trap(self, height: List[int]) -> int:
        # each place can hold min(left_max, right_max) - height
        # can precompute this which takes O(n) time and space
        # can do this on the fly, taking O(1) space and O(n) time

        left_max = 0
        right_max = 0

        l, r = 0, len(height) - 1
        res = 0 

        while l < r:
            if height[l] <= height[r]:
                if left_max < height[l]:
                    left_max = height[l]
                else:
                    res += left_max - height[l]
                l += 1
            else:
                if right_max < height[r]:
                    right_max = height[r]
                else:
                    res += right_max - height[r]
                r -= 1

        return res