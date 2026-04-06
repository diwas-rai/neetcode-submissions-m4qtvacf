class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        t_char_to_count = defaultdict(int)
        for c in t:
            t_char_to_count[c] += 1
        
        have = 0
        need = len(t_char_to_count)
        res = [float('inf'), -1, -1]
        l = 0
        s_char_to_count = defaultdict(int)

        for r in range(len(s)):
            curr_char = s[r]

            s_char_to_count[curr_char] += 1
            if (curr_char in t_char_to_count and
                t_char_to_count[curr_char] == s_char_to_count[curr_char]):
                have += 1
            
            while l <= r and have == need:
                if r - l + 1 > 0 and r - l + 1 < res[0]:
                    res = [r - l + 1, l, r]

                s_char_to_count[s[l]] -= 1
                if s[l] in t_char_to_count and s_char_to_count[s[l]] < t_char_to_count[s[l]]:
                    have -= 1
                l += 1
        
        resLen, resL, resR = res
        return s[resL : resR + 1] if resLen != float('inf') else ""


