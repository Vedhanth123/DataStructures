class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        total_profit = 0
        low = prices[0]
        high = prices[0]

        i = 0
        # compare the adjacent elements
        while(i < len(prices)-1):

            # find the local minima
            while(i < len(prices)-1 and prices[i] >= prices[i+1]):
                i += 1
            low = prices[i]

            # find the local maxima
            while(i < len(prices)-1 and prices[i] <= prices[i+1]):
                i += 1
            high = prices[i]


            total_profit += high - low
        
        return total_profit