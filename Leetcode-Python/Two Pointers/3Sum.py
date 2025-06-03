# Two Pointer Solution:
class Solution:
    def threesum(self, nums: list[int]) -> list[list[int]]:
        sol = []
        nums.sort()

        for i, num in enumerate(nums):
            if num > 0:
                # if num > 0 then this is guaranteed not be greater than 0
                # and so not a solution (solution are equal to 0)
                break
            if num == nums[i-1]:
                # we want unique triplets so if this condition is met,
                # the triplet cannot be uniue as the list is in order
                continue
            left = i + 1
            # we set to i + 1 because we are fixing some number (num) and then
            # doing a two pointer to adjust all the sum iterations of that number
            # until we find all combinations it can be, then move to next num
            right = len(nums) - 1
            while left < right:
                # We adjust our threesum keeping num fixed until next loop iteration
                # check all iterations using two pointer (adjust towards solution)
                # depending on if the threesum is too big or too small.
                
                threesum = num + nums[left] + nums[right]
                if threesum > 0:
                    right -= 1
                elif threesum < 0:
                    left += 1
                else:
                    sol.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # To ensure the next solution is unique we have this while
                    # Otherwise we could just have repeated solutions if number after
                    # left and before right is the same number.
                    while nums[left] == nums[left -1] and left < right:
                        left += 1
        return sol

obj = Solution()

sol = obj.threesum([-1,0,1,2,-1,-4])

print(sol)

# Brute Force Solution
class Solution:
    # Only thing to be careful of here is to use ranges so that you can
    # take out the indexes and therefore add them as a tuple to the set.
    # Also, ensure that you add a tuple to the set not a list lol.
    def threeSumBrute(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        sol = set()

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    threesum = nums[i] + nums[j] + nums[k]
                    if threesum == 0:
                        sol.add(tuple(nums[i], nums[j], nums[k]))
        return sol