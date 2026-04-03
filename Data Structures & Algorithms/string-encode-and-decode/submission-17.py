class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + '#' + s

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        i, j = 0, 0
        res = []

        while i < len(s) and j < len(s):
            while s[j] != '#':
                j += 1
            
            word_len = int(s[i:j])

            j += 1
            i = j
            j += word_len

            res.append(s[i:j])
            i = j
        
        return res