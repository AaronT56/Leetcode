class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max(nums)
        # We use two variable, the reason for this is to account for negative values,
        # the most negative value in our array will be held at the min. This means if 
        # we encounter another negative value in nums, the sign will switch, and this
        # min has potential to become our max (and max become min). It's important to
        # track this.
        curMin, curMax = 1, 1

        for n in nums:
            # We save tmp because we want the current curMax not the one after the next
            # line of code.
            tmp = curMax * n
            # We need to keep n here because in some edge cases like an array [-1, 8]
            # n will be the largest.
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(tmp, curMin * n, n)
            res = max(res, curMax)
        return res
        