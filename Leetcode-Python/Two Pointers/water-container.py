class Solution:
    def maxArea(self, heights: list[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0
        while left < right:
            h = min(heights[left], heights[right])
            w = right - left
            max_area = max(max_area, h * w)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area
    
obj = Solution()

res = obj.maxArea([1,8,6,2,5,4,8,3,7])

print(res)

