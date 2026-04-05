class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_to_freq = defaultdict(int)
        l = 0
        max_freq = 0
        max_len = 0

        for r in range(len(s)):
            char_to_freq[s[r]] += 1
            max_freq = max(max_freq, char_to_freq[s[r]])

            while r - l + 1 - max_freq > k:
                char_to_freq[s[l]] -= 1
                l += 1
            
            max_len = max(max_len, r - l + 1)
    
        return max_len