from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        output = []
        # If an element on the left is less than an element on 
        # the right of it, we know it will
        # never be a maximum. This algorithm takes advantage of that and excludes it from
        # the next search, so even if k = 3 we might only be searching 2 elements which
        # speeds things up.
        # We use a deque because a deque allows us to pop from the front and the back.
        q = deque() # We are gonna just have this be indices, important for later.
        l = r = 0
        
        for r in range(len(nums)):
            # You can see here, that we are popping all the elements lower than our 
            # current nums[r]. This means they will not be in our queue in the future which
            # is useful for efficiency.
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # This works because our queue is a bunch of indices. If l is outside
            # the bounds of our indices, we pop it. This is just making sure that the
            # list when adjusted gets rid of the indexes outside of our current window that
            # would be captured by k. 
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                # So once r has reached the point that it is at k, we start appending
                # our nums[q[0]] (the largest element due to the first loop)
                # we also start increasing our l for the rest of the loop.
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output