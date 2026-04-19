class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        t_char_to_count = Counter(t)
        s_char_to_count = defaultdict(int)

        l = 0
        res = [-1, -1, float('inf')] # l, r, len
        need, have = len(t_char_to_count), 0

        for r in range(len(s)):
            curr_char = s[r]
            s_char_to_count[curr_char] += 1

            if (curr_char in t_char_to_count and 
                s_char_to_count[curr_char] == t_char_to_count[curr_char]):
                have += 1
            
            while have == need:
                if r - l + 1 < res[2]:
                    res = [l, r, r - l + 1]
                s_char_to_count[s[l]] -= 1
                if s_char_to_count[s[l]] < t_char_to_count[s[l]]:
                    have -= 1
                l += 1

        return s[res[0] : res[1] + 1] if res[2] != float('-inf') else ""
            


        
