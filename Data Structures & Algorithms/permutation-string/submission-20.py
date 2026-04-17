"""
s2 contains premutation of s1?
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_char_to_count = {}
        for c in s1:
            s1_char_to_count[c]= s1_char_to_count.get(c, 0) + 1

        s2_char_to_count = {}
        l = 0
        for r, c in enumerate(s2):
            s2_char_to_count[c] = s2_char_to_count.get(c, 0) + 1 

            if r - l + 1 > len(s1):
                s2_char_to_count[s2[l]] -= 1
                if s2_char_to_count[s2[l]] == 0:
                    del s2_char_to_count[s2[l]]
                l += 1
            
            if s1_char_to_count == s2_char_to_count:
                return True
            
        return False
