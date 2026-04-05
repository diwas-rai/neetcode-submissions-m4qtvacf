class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1_char_to_count = defaultdict(int)
        s2_char_to_count = defaultdict(int)
        for i in range(len(s1)):
            s1_char_to_count[s1[i]] += 1
            s2_char_to_count[s2[i]] += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if s1_char_to_count == s2_char_to_count:
                return True
            
            s2_char_to_count[s2[l]] -= 1
            if s2_char_to_count[s2[l]] == 0:
                del s2_char_to_count[s2[l]]
            l += 1
            s2_char_to_count[s2[r]] += 1

        if s1_char_to_count == s2_char_to_count:
            return True
        
        return False