class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        L = 0
        R = 1
        max_profit = 0
        while(L < len(prices) and R < len(prices)):

            max_profit = max(max_profit, prices[R] - prices[L])
            if(prices[R] < prices[L]):
                L = R
                R += 1
            else:
                R += 1
        
        return max_profit