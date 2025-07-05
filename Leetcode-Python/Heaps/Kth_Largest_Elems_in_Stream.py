import heapq
class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.minHeap, self.k = nums, k
        # the key of the minheap is that the smallest value with always be at the
        # beginning even if you pop. So for this question we want the k'th largest,
        # so we just pop (from the bottom as is normal with heaps) until there is just
        # the largest k left. And then check heap[0] and boom.
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int):
        heapq.heappush(self.minHeap, val)
        # This just ensures that given the heap has gone too big and no longer
        # contains k elements, we pop it to bring it back to its original number
        # of elements which is k or less.
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        # So this array stores the n largest elements. So the 0 will always be the kth
        # largest element. It works out well :). When you pop, you remove the first 
        # element, but when you do that, the next biggest element shifts down to the
        # bottom. Note that ONLY this element will go down. One side of the tree will
        # change only (doesn't matter how)
        return self.minHeap[0]