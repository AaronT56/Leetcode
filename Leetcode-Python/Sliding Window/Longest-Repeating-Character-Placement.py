from typing import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = 0
        maxf = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] += 1
            # Finds the current most frequent element in our dictionary
            maxf = max(maxf, count[s[r]])
            # So now we take remove invalid elements from our window till it becomes valid.
            # So we take the length of the window - maxf and see if it is bigger than k
            # If it is bigger then the window is no longer valid and we must start removing
            # elements from the window.
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res