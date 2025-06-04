"""Given an unsorted array of integers nums, return the length of the longest consecutive 
elements sequence.

You must write an algorithm that runs in O(n) time."""
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = sorted(nums)
        longest = 1
        res = 1
        if not nums:
            return 0
        
        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                longest += 1
                if longest > res:
                    res = longest
            elif nums[i] == nums[i+1]:
                longest += 0
            else:
                longest = 1
            
        return res
                    
    
obj = Solution()

obj.longestConsecutive([1,5,3,2,4,9,4,12,23,50,-10,6])