class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []

        l, r = 0, 0
        while r < len(s):
            while r < len(s) and s[r] != '#':
                r += 1
            
            word_len = int(s[l:r])
            l = r + 1
            r = l + word_len

            res.append(s[l:r])

            l = r

        return res

