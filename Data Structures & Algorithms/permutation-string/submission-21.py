class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        window = defaultdict(int)
        s1_count = defaultdict(int)

        for i in range(len(s1)):
            window[s2[i]] += 1
            s1_count[s1[i]] += 1
        
        matches = 0 
        for i in range(26):
            c =  chr(ord('a') + i)
            if window[c] == s1_count[c]:
                matches += 1
        
        if matches == 26:
            return True
        
        l = 0
        for r in range(len(s1), len(s2)):
            c = s2[r]
            window[c] += 1
            if window[c] == s1_count[c]:
                matches += 1
            elif window[c] == s1_count[c] + 1:
                matches -= 1

            c = s2[l]
            window[c] -= 1
            if window[c] == s1_count[c]:
                matches += 1
            elif window[c] == s1_count[c] - 1:
                matches -= 1
            l += 1

            print(s2[l:r+1], matches)
            if matches == 26:
                return True
        
        return matches == 26