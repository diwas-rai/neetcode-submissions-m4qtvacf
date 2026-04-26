class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = defaultdict(int)
        for c in t:
            t_count[c] += 1
        
        have, need = 0, len(t_count)
        l = 0
        res = [0, 0]
        res_len = float('inf')
        s_count = defaultdict(int)
        for r in range(len(s)):
            s_count[s[r]] += 1
            if s[r] in t_count and s_count[s[r]] == t_count[s[r]]:
                have += 1
            
            while have == need and l <= r:
                if r - l + 1 < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                s_count[s[l]] -= 1
                if s[l] in t_count and s_count[s[l]] == t_count[s[l]] - 1:
                    have -= 1
                l += 1

        
        return s[res[0] : res[1] + 1] if res_len != float('inf') else ""