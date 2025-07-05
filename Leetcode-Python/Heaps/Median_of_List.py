import heapq
class MedianFinder:

    def __init__(self):
        self.large = []
        self.small = []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            val = -1 * num
            heapq.heappush(self.small, val)
        
        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * val)
        if len(self.large) > len(self.small) + 1:
            val = -1 * heapq.heappop(self.large)
            heapq.heappush(self.small, val)

    def findMedian(self) -> float:
        
        if len(self.small) > len(self.large):
            return self.large[0]
        
        if len(self.large) > len(self.small):
            return self.small[0]
        
        return (-1 * self.small[0] + self.large[0]) / 2.0