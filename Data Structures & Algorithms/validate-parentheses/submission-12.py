class Solution:
    def isValid(self, s: str) -> bool:
        closed_to_open = {"}":"{", ")": "(", "]":"[" }
        stk = []

        for c in s:
            if c in closed_to_open:
                if stk and stk[-1] == closed_to_open[c]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)
        
        return not stk