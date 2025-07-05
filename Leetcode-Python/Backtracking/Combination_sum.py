class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        res = []
        sum_parts = []

        def dfs(i, sum_parts):
            total = sum(sum_parts)
            if total == target:
                res.append(sum_parts.copy())
                return
            
            if i >= len(nums) or total > target:
                return
            
            # The way these loops work is they essentially build a list of nums[0] and 
            # then once this is built, we track backwards through the list and pop last
            # element of nums[0] list and iterate through all of the possible options 
            # checking until they are > target. Eventually we will go through all possible
            # iterations.
            sum_parts.append(nums[i])
            dfs(i, sum_parts)

            sum_parts.pop()
            dfs(i + 1, sum_parts)
        
        dfs(0, sum_parts)
        return res