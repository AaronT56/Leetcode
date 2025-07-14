class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        if intervals == []:
            return True
        
        intervals.sort(key = lambda i: i.start)
        prevEnd = intervals[0].end

        for i in range(1, len(intervals)):
            start = intervals[i].start
            end = intervals[i].end
            if prevEnd > start:
                return False
            
            else:
                prevEnd = end
        
        return True