class Solution:

    def encode(self, strs: list[str]) -> str:
        out = ""
        for word in strs:
            out += len(word) + '#' + word

        return out
    
    def decode(self, s: str) -> list[str]:
        i = 0
        res = []
        for j in range(s):
            if s[j] == '#':
                length = s[j - 1]
                i = length + 1
                word = s[j:i]
                i = j
                res.append(word)
        return res
    
obj = Solution

enc = obj.encode(["neet","code","love","you"])

print(enc)
