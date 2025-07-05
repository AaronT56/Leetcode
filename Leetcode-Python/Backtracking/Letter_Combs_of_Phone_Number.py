# My original Solution but it's a bit clunky so I have neetcode solution too
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        parts = []
        if not digits:
            return res

        jump = ord('a')
        letters = {}
        i = 0
        for digit in range(2, 10):
            letters[digit] = [chr(i + jump), chr(i + jump + 1), chr(i + jump + 2)]
            if digit == 7 or digit == 9:
                letters[digit].append(chr(i + jump + 3))
                i += 1
            i += 3

        def dfs(i):
            if i >= len(digits):
                res.append("".join(c for c in parts))
                return
            
            num = int(digits[i])
            for letter in letters[num]:
                parts.append(letter)
                dfs(i + 1)
                parts.pop()

        dfs(0)
        return res

# Neetcode Solution. More manual but readable and just better
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)
            
        if digits:
            backtrack(0, "")
        
        return res
