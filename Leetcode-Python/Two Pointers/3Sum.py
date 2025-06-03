class Solution:
    def threesum(self, nums: list[int]) -> list[list[int]]:
        sol = []
        nums.sort()

        for i, num in enumerate(nums):
            if num > 0:
                break
            if num == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                threesum = num + nums[left] + nums[right]
                if threesum > 0:
                    right -= 1
                if threesum < 0:
                    left += 1
                else:
                    sol.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left -1] and left < right:
                        left += 1
        return sol

obj = Solution()

sol = obj.threesum([-1,0,1,2,-1,-4])

print(sol)
