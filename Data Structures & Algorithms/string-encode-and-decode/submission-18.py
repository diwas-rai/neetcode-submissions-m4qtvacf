class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            res.append(str(len(s)) + '#' + s)

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []

        j = 0
        while j < len(s):
            i = j
            while s[j] != '#' and j < len(s):
                j += 1

            word_len = int(s[i:j])
            j += 1
            i = j
            j = i + word_len
            word = s[i:j]
            res.append(word)
        
        return res