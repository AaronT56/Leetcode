class Solution:
    # Dictionary Solution
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        nummap = {}
        for i, num in enumerate(numbers):
            lookup = target - num
            if lookup in nummap:
                return [nummap[lookup], i]
            nummap[num] = i
            
class Solution:
    # Two-Pointer Solution
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            s = numbers[right] + numbers[left]
            if s == target:
                return [left+1, right+1]
            elif s < target:
                left += 1
            else:
                right -= 1

                 