class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        # one = number of ways to reach current step (dp[i])
        # two = number of ways to reach previous step (dp[i-1])
        for i in range(n - 1):
            tmp = one
            one = one + two # dp[i + 1] = dp[i] + dp[i - 1]
            two = tmp
        
        return one