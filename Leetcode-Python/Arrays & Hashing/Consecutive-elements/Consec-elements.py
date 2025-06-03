"""Given an unsorted array of integers nums, return the length of the longest consecutive 
elements sequence.

You must write an algorithm that runs in O(n) time."""
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        order = sorted(nums)
        ans = 0
        check = 1
        for i in range(len(order)-1):
            if order[i+1] == order[i] + 1:
                check += 1
                if check > ans: 
                    ans = check
            elif order[i+1] == order[i]:
                check += 0
            else:
                check = 1
        return ans
                    
    
obj = Solution()

obj.longestConsecutive([1,5,3,2,4,9,4,12,23,50,-10,6])