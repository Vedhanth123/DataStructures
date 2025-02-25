class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        mini = prices[0]
        for x in range(1,len(prices)):

            cost = prices[x] - mini
            profit = max(profit, cost)
            mini = min(mini, prices[x])
        
        return profit