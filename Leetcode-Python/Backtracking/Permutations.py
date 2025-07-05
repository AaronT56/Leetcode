class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        self.res = []
        self.backtrack(nums, 0)
        return self.res

    def backtrack(self, nums: list[int], idx):
        if idx == len(nums):
            self.res.append(nums.copy())
            return
        
        # Note the range. We are iterating through swapping the elements each time. Early
        # on we are just swapping some element with that same element. But taking idx = 0
        # for example, we will be swapping element 0 with each value of i up till len(nums)
        # which covers all iterations.
        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]
            self.backtrack(nums, idx + 1)
            nums[idx], nums[i] = nums[i], nums[idx]