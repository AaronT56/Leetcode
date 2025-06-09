class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r-l)//2
            if target == nums[m]:
                return m
            
            elif nums[l] <= nums[m]:
                if target < nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            
            elif nums[l] > nums[m]:
                if target > nums[r] or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            
        return -1 


            

         

obj = Solution()

obj.search([3,4,5,6,1,2], 1)