from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        output = []
        q = deque()
        l = r = 0
        
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if l < q[0]:
                q.popleft()

            if l < q[0]:
                q.popleft()

            if (r + 1) <= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output