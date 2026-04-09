class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        left_maxes = [0] * n
        max_left = 0
        for i in range(n):
            max_left = max(max_left, height[i])
            left_maxes[i] = max_left
        
        right_maxes = [0] * n
        max_right = 0
        for i in range(n-1, -1, -1):
            max_right = max(max_right, height[i])
            right_maxes[i] = max_right
    
        total = 0
        for i in range(n):
            total += min(left_maxes[i], right_maxes[i]) - height[i]
        
        return total