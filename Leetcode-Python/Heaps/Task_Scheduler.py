from collections import Counter
import deque
import heapq
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        count = Counter(tasks)

        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0

        q = deque()

        while maxHeap or q:
            # If there is tasks remaining in maxHeap or remaining in the queue (waiting to
            # be able to be processed) then we keep going and add time.
            time += 1

            if maxHeap:
                # If there is a value in maxHeap, we add one to that value (so we know 
                # that we have processed it one more time) and then we keep going. We add
                # rather than subtract as the maxHeap requires values to be negative.
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    # So we save the task that was just processed and at it to the queue,
                    # accounting for how much time until we can process it again (n).
                    q.append([cnt, time + n])
                    
                # if we are allowed to again process the task again, then we add it
                # back to our maxheap to be processed
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time