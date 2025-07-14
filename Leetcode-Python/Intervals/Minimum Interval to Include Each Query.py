# General method: Go through every query, check what intervals that query is valid,
# we pop the invalid intervals, (because we add all queries with start big enough
# to be included in interval so some ends < q) then finally, assign res to smallest 
# value that is left in minHeap
import heapq
class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        intervals.sort()
        res = {}
        minHeap = []
        i = 0

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] < q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1
            
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            res[q] = minHeap[0][0] if minHeap else -1
        
        return [res[q] for q in queries]
