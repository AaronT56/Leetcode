"""Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9)."""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = s.lower()
        ans = ''.join(c for c in ans if c.isalnum())
        palindrome = ans[::-1]
        if(ans == palindrome):
            print(palindrome)
            return True
        return False


obj = Solution()

res = obj.isPalindrome("0P")

print(res)