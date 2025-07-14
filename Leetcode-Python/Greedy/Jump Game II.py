class Solution:
    def jump(self, nums: list[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            # We essentially save in groups of jumps. So we see how far we can jump,
            # and then based on the furthest we can jump from there, we again iterate
            # between the r + 1 index and the furthest distance, and see how far we
            # can jump out of that group, and repeat until end. It's simple just 
            # remember the nums[i] + i thing.
            for i in range(l, r + 1):
                farthest = max(farthest, nums[i] + i)

            l = r + 1
            r = farthest
            res += 1
        
        return res
        