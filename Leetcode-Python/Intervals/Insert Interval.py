class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            else:
                # While we have for example intervals = [[1,3],[1,5],[6,7]] and
                # newInterval = [2, 5], you want output of [1, 6]. Essentially, we keep
                # having this function calling whil we iterate through different i values
                # and finally we append once we get for example newInterval[1] < 
                # intervals[i][0]. So we don't add to res until this condition is met or
                # list ends. This allows us to get the above solution using commands like
                # the one below. I don't know I can't explain in words just look at code
                # and think.
                newInterval = [min(newInterval[0], intervals[i][0]),
                               max(newInterval[1], intervals[i][1])]
                
        res.append(newInterval)
        return res
    