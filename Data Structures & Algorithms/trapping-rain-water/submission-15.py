class Solution:
    def trap(self, height: List[int]) -> int:
        # each place can hold min(left_max, right_max) - height
        # can precompute this which takes O(n) time and space
        # can do this on the fly, taking O(1) space and O(n) time

        left_max = [0] * len(height)
        right_max = [0] * len(height)

        for i in range(1, len(height) - 1):
            left_max[i] = max(left_max[i-1], height[i-1])

        for i in range(len(height) - 2, - 1, -1):
            right_max[i] = max(right_max[i+1], height[i+1])
        
        res = [1] * len(height)

        for i in range(len(height)):
            res[i] = max(min(left_max[i], right_max[i]) - height[i], 0)

        return sum(res)