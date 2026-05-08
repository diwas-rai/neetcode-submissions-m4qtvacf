class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        l = 0
        freqs = defaultdict(int)

        for r in range(len(s)):
            freqs[s[r]] += 1
            
            while freqs[s[r]] > 1:
                freqs[s[l]] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)

            
        return max_len