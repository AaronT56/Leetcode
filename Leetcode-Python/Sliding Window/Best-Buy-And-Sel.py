class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1
        curmax = 0
        while r < len(prices):
            # create window and see if the left element is less than right. If so
            # keep adding to right until you find a max and then you can sell. So
            # we will find the lowest on the left and highes to the right of that left.
            if prices[l] < prices[r]:
                profit = prices[l] - prices[r]
                curmax = max(curmax, profit)
            else:
                l = r
            r += 1
        return curmax
            
