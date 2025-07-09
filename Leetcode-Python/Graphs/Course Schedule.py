class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        visit = set()

        preMap = {i:[] for i in range(numCourses)}

        for crs, prq in prerequisites:
            preMap[crs].append(prq)

        def dfs(crs):
            # So we throw our pre-reqs into this function, if a pre-req is required for
            # a course to be done, but the course also requires the pre-requisite,
            # then this will trigger here and we will return False. Remember, what is
            # input here is all pre-requisites of stuff that is in visit. Like for each
            # dfs call we are exploring a crs. If we encounter it again, then there must
            # be a cycle.
            if crs in visit:
                return False
            
            if preMap[crs] == []:
                return True
            
            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False

            # Note that we remove crs from the cycle and make it empty because
            # it has passed our prerequisite test and we only really want to track the 
            # node on the current recursion stack, not even node ever. So if it passes
            # the loop without returning False then we can set it to empty (we haven't) 
            # actually adjusted it until this point so we need to change it now for future
            # recursion stacks to work properly and we know it is valid so it can just
            # be set to have no prerequisites.
            
            visit.remove(crs)
            preMap[crs] = []
            return True
        
        # The courses are all just numbers. So we iterate through each number. If we
        # get True outputs for all numbers, then each course can be done using the 
        # prerequisites, and we output True. 
        # So when we run this function, the dfs checks, can we get through this prereq
        # chain? If so, we continue.
        for crs in range(numCourses):
            if not dfs(crs): return False

        return True