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
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])
            if height[l] <= height[r]:
                res += max(min(left_max, right_max) - height[l], 0)
                l += 1
            else:
                res += max(min(left_max, right_max) - height[r], 0)
                r -= 1

        return res