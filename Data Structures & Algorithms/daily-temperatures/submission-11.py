class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stk and stk[-1][0] < temp:
                stk_temp, stk_idx = stk.pop()
                res[stk_idx] = i - stk_idx
            
            stk.append([temp, i])

        return res