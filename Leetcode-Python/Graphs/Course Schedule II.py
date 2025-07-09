class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i : [] for i in range(numCourses)}
        seen, cycle = set(), set()

        for crs, prq in prerequisites:
            preMap[crs].append(prq)

        res = []

        def dfs(crs):
            # This essentially confirms that we have looked at this course and confirm
            # that it is indeed chilling and we can skip through it as it does have
            # all the required prerequisites.
            if crs in seen:
                return True
            if crs in cycle:
                return False
            
            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            cycle.remove(crs)
            seen.add(crs)
            res.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return res
            