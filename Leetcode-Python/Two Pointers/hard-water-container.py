class Solution:
    def trap(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        leftmax, rightmax = height[l], height[r]
        res = 0

        while l < r:
            if height[l] <= height[r]:
                l += 1
                leftmax = max(leftmax, height[l])
                res += leftmax - height[l]

            else:
                r -= 1
                rightmax = max(rightmax, height[r])
                res += rightmax - height[r]

        return res