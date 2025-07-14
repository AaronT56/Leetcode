class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda i: i[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = res[-1][1]

            if start <= lastEnd:
                lastEnd = max(end, lastEnd)
                res[-1][1] = lastEnd
            
            else:
                res.append([start, end])
            
        return res
