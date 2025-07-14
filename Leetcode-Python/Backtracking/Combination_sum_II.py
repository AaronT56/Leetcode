class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        summers = []
        res = []
        candidates.sort()

        def dfs(i, summers, total):
            if total == target:
                res.append(summers.copy())
                return
            
            if i >= len(candidates) or total > target:
                return
            
            summers.append(candidates[i])
            dfs(i + 1, summers, total + candidates[i])

            summers.pop()
            # This ensures you only explore one exclude path per unique number, and that's
            # what prevents duplicate combinations from being created. Think in terms of 
            # what these omitted lists will look like. As long as we don't have duplicates
            # in them, there cannot be any lists which are the same as the ones created
            # on the way up.
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            # The key understanding here, is that we are trying the same thing but this 
            # we are essentially saying, what if we never added that number in total in
            # the first place? That's why total is not adjusted. So we have two iterations,
            # one where we have the duplicates, and one where we have no duplicates and 
            # by saying, hey, if we never added that number we just added, what
            # would happen? Remember this total is the total we had before we added nums[i]
            # to the above function so we are essentially going back to that original total
            # and continuing seeing what goes on afterwards.
            dfs(i + 1, summers, total)
        
        dfs(0, [], 0)
        return res