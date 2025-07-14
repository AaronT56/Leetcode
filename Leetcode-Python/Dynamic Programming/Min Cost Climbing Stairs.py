class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        # We are going to check from each point starting at the end of the list, what
        # the cheapest way to get to that point was and the total cost at each point
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])