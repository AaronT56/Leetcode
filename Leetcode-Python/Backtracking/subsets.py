from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                # We use subset.copy() because list objects are mutable in python so
                # we must be careful here.
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()

            dfs(i + 1)
        
        dfs(0)
        return res