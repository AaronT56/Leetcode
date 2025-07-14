class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            # all numbers after i (if there are any bigger numbers we should
            # save them)
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    # Sometimes the bigger value at j = 5 will
                    # be bigger than the values at for example
                    # j = 6. Say for example j = 6 is a huge 
                    # number like 105 then it will be small in 
                    # LIS, yet j = 5 is bigger than cur LIS[i]
                    # but not so big, so it will have more
                    # bigger numbers after
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        
        return max(LIS)