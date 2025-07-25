import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            time = 0

            for p in piles:
                time += math.ceil(p/k)
            
            if time <= h:
                res = k
                r = k - 1

            elif time > h:
                l = k + 1
        return res

