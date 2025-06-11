class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        maxArea = 0
        stack = [] # pair: (index, height)
        for i, h in enumerate(heights):
            start = i # keep track of left boundary
            # Because the once this condition is met, all stack[-1][1] > h will
            # no longer contribute to the rectangle, so we can find the area that
            # they covered and then continue on our way. (see if that area was max first
            # tho!)
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index #  we extend this bar to the left as far as we popped
            stack.append((start, h)) # we append the new height and how far back that new
            # height is "valid"

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights)- i))

        return maxArea
    