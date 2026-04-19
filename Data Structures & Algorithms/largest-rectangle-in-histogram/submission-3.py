class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stk = [] # (height, start)

        for i, h in enumerate(heights):
            start = i
            while stk and stk[-1][0] > h:
                stk_h, stk_i = stk.pop()
                res = max(res, stk_h * (i - stk_i))
                start = stk_i
            stk.append((h, start))
            
        for h, i in stk:
            res = max(res, h * (len(heights) - i))
        
        return res