class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda i:i[1])
        overlaps = 0
        curLast = intervals[0][1]

        for start, end in intervals[1:]:
            if start < curLast:
                overlaps += 1
            
            else:
                curLast = end
        
        return overlaps