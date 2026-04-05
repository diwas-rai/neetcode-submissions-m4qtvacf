class Solution:
    def trap(self, height: List[int]) -> int:
        # for each position determine the tallest wall to the left and right
        # the minimum of those two determine how much water a position can hold
        # then subtract the value of height[i] at the current position
        n = len(height)

        max_on_left = [0] * n
        max_l_value = 0
        for i in range(1, n):
            max_l_value = max(height[i - 1], max_l_value)
            max_on_left[i] = max_l_value

        max_on_right = [0] * n
        max_r_value = 0
        for i in range(n - 2, -1, -1):
            max_r_value = max(height[i + 1], max_r_value)
            max_on_right[i] = max_r_value
        
        res = 0
        for i in range(n):
            res += max(min(max_on_left[i], max_on_right[i]) - height[i], 0)

        return res