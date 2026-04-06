class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        max_area = 0

        for i, height in enumerate(heights):
            start = i
            while stk and stk[-1][0] > height:
                stk_h, stk_idx = stk.pop()
                max_area = max(max_area, stk_h * (i - stk_idx))
                start = stk_idx

            stk.append([height, start])

        while stk:
            stk_h, stk_idx = stk.pop()
            max_area = max(max_area, stk_h * (1 + len(heights) - 1 - stk_idx))

        return max_area