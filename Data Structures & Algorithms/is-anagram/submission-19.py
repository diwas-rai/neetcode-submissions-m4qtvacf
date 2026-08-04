class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        t_chars = {}
        s_chars = {}

        for i in range(len(t)):
            t_chars[t[i]] = t_chars.get(t[i], 0) + 1
            s_chars[s[i]] = s_chars.get(s[i], 0) + 1
        
        for c in s:
            if s_chars[c] != t_chars.get(c, 0):
                return False
        
        return True