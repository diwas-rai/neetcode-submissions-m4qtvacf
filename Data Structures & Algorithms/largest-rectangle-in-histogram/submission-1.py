class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        largest_area = 0

        for i, height in enumerate(heights):
            start = i
            while stk and stk[-1][1] > height:
                stk_start, stk_height = stk.pop()
                largest_area = max(largest_area, (i - stk_start) * stk_height)
                start = stk_start
            stk.append([start, height])

        while stk:
            stk_start, stk_height = stk.pop()
            largest_area = max(largest_area, (len(heights) - stk_start) * stk_height)

        return largest_area