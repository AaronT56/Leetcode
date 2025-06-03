class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = [1] * len(nums)

        left = 1
        for i in range(len(nums)):
            ans[i] *= left
            left *= nums[i]

        right = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= right
            #print(ans, nums[i])
            right *= nums[i]
            
        return ans

obj = Solution()

res = obj.productExceptSelf([5, 10, 15])

print(res)