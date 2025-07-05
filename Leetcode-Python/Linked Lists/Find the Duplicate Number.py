class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow, fast = 0, 0

        # The purpose of this loop is to find that there is 
        # in fact a loop and how far into the list (slow) will be exactly
        # half way through this loop. Further nums[fast] will always be valid as
        # we are bounded by [1,n] (read question).
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Once we have found our value we can find the exact point where the duplicate was
        # found by iterating through slow2 until slow2 == slow. The reason is because
        # fast was found at exactly double the length of slow. So by iterating from where
        # slow starts and 0 where everything starts, the two values will be equal at the 
        # duplicate value.
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow