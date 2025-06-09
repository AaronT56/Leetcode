from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        if t == "":
            return ""
        
        countT, window = defaultdict(int), defaultdict(int)
        for c in t:
            countT[c] += 1

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] += 1

            # This will just update if the newly added element of our string is
            # equivalent to one of the elements in t. I think the second condition
            # is incase there are multiple c you need for example if you need to have 2
            # of some given letter.
            if c in countT and window[c] == countT[c]:
                have += 1

            # So this is if we actually meet the condition that we want
            while have == need:
                # Save our initial solution. Then we start removing and see if we can make
                # our interval smaller. While we can these results will update.
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # so if we actually meet the condition, we remove from the left and see if
                # the removed element is in counT. If not, we keep removing until slowly we find
                # the smallest list. If it's not part of t we keep going until it is.
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l: r + 1] if resLen != float("infinity") else ""

    
obj = Solution()

res = obj.minWindow("OUZODYXAZV", "XYZ")

print(res)
        