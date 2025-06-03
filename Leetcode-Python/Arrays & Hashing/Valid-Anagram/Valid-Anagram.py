class Solution:
    def isAnagram(self, s: str, t: str) -> str:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        return sorted_s == sorted_t

obj = Solution()

obj.isAnagram("anagram", "nagaram")


