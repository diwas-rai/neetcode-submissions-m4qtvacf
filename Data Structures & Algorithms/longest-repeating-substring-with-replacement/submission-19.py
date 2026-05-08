class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_f = 0
        max_len = 0
        char_counts = defaultdict(int)
        l = 0

        for r in range(len(s)):
            char_counts[s[r]] += 1
            max_f = max(max_f, char_counts[s[r]])

            while r - l + 1 - max_f > k:
                char_counts[s[l]] -= 1
                l += 1
            
            max_len = max(max_len, r - l + 1)
        
        return max_len
