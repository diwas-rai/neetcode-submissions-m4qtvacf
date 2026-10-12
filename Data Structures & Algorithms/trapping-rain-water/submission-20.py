class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        left_max = 0
        right_max = 0
        res = 0

        l, r = 0, n - 1
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
