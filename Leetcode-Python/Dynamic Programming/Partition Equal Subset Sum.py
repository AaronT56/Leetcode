class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        # if sum is odd, then we can't cleanly split array because odd can only
        # arise from adding odd + even
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        # We can go backwards or forwards doesn't matter he just did backwards
        for i in range(len(nums) - 1, -1, -1):
            # We use this set just for safety, you can technically just use dp always
            # but this method is a bit cleaner and less bug prone.
            nextDP = set()
            for t in dp:
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return True if target in dp else False
