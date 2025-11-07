from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = prices[0]
        profit = float('-inf')

        for x in range(1, len(prices)):

            if(prices[x] < min_price):
                min_price = prices[x]
            
            profit = max(profit, prices[x] - min_price)
        
        return profit

obj = Solution()
obj.maxProfit([7,6,4,3,1])