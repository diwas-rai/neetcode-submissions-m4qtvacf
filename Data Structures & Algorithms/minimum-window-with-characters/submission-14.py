class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        t_char_to_count, window = defaultdict(int), defaultdict(int)
        for c in t:
            t_char_to_count[c] += 1
        
        have, need = 0, len(t_char_to_count)
        res = [float('inf'), -1, -1]
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] += 1

            if c in t_char_to_count and window[c] == t_char_to_count[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < res[0]:
                    res = [r-l+1, l, r]
                
                window[s[l]] -= 1
                if s[l] in t_char_to_count and window[s[l]] < t_char_to_count[s[l]]:
                    have -= 1

                l += 1

        length, l, r = res
        return s[l : r + 1] if length != float('inf') else ""