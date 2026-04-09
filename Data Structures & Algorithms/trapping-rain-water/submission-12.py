class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) -1 
        left_max = height[l]
        right_max = height[r]
        total = 0
        while l <= r:
            if left_max < right_max:
                total += left_max - height[l]
                l += 1
                left_max = max(left_max, height[l])
            else:
                total += right_max - height[r]
                r -= 1
                right_max = max(right_max, height[r])

        return total