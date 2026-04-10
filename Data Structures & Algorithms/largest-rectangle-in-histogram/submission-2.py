class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = [] # (height, start)
        res = 0

        for i, h in enumerate(heights):
            start = i

            while stk and stk[-1][0] > h:
                stk_h, stk_idx = stk.pop()
                res = max(res, (i - stk_idx) * stk_h)
                start = stk_idx
            
            stk.append((h, start))
        
        while stk:
            stk_h, stk_idx = stk.pop()
            res = max(res, (len(heights) - stk_idx) * stk_h)

        return res