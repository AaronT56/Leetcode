class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        jump_len = 1
        for i in range(len(nums) - 2, -1, -1):
            if jump_len <= nums[i]:
                goal = i
                jump_len = 1
                
            else:
                jump_len += 1
        
        return goal == 0