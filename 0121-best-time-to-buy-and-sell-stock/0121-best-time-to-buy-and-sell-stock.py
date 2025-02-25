class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        lowest_val = prices[0]


        for x in range(1, len(prices)):

            profit = max(profit, prices[x] - lowest_val)
            lowest_val = min(lowest_val, prices[x])
        
        return profit