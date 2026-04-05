class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        # expand window when condition not fulfilled
        # shrink window when condition is fulfilled
        # condition -> t's letters are present in s

        t_char_to_count = defaultdict(int)
        for c in t:
            t_char_to_count[c] += 1
        
        l = 0
        ans = ""
        min_length = float('inf')
        s_char_to_count = defaultdict(int)
        for r in range(len(s)):
            t_present = True
            s_char_to_count[s[r]] += 1
            for c in t_char_to_count.keys():
                if t_char_to_count[c] > s_char_to_count.get(c, 0):
                    t_present = False
                
            while l <= r and t_present:
                if r - l + 1 >= 1 and r - l + 1 < min_length:
                    ans = s[l:r+1]
                    min_length = r - l + 1
                s_char_to_count[s[l]] -= 1
                l += 1
                for c in t_char_to_count.keys():
                    if t_char_to_count[c] > s_char_to_count.get(c, 0):
                        t_present = False
        
        return ans
