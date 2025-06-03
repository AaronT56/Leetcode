class Solution:
    def encode(self, strs: list[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + '#' + word
        return res
    
    def decode(self, s: str) -> list[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            if s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res
