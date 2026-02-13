from typing import List

# This problem is a classic state machine problem.
# for each index you have two states (not choices) choices are those which you have nonetheless of the situation.

# let me give you an example of what a choice is and what a state is
# for example if you are standing at nth index you have choice of not robbing the house and robbing the house
# But.. in this case you have two states (you can't sell the stock unless you buy it. Meaning your choices are dependent on the state you are in right now.)


# so.. the two states we have right now are
# 1) buy -> (you have to buy the stock but... you have two choices (you could buy it or you could not buy it)
#    ->   If you buy the stock then pay for it and you can't buy it again.
#    ->   If you don't buy the stock then you don't pay but.. you can buy it later

# 2) sell -> (you can sell the stock (but... you have 2 choices. You could sell the stock or you could keep it with yourself))
#    ->   If you sell the stock then you receive the rewards and you can buy the stock again
#    ->   If you don't sell the stock then you won't receive the rewards and you can't buy the stock again.


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        # recursion + memoization
        '''

        n = len(prices)

        memo = {}

        def rec(index, buy):

            if((index, buy) in memo):
                return memo[(index, buy)]

            if(index == n):
                return 0
            
            profit = 0
            if(buy):

                profit = max(
                    -prices[index] + rec(index+1, 0),
                    rec(index+1, 1)
                )
            else:
                profit = max(
                    prices[index] + rec(index+1, 1),
                    rec(index+1, 0)
                )
            
            memo[(index, buy)] = profit
            return memo[(index,buy)]
        
        return rec(0,1)
        '''
        # bottom up (tabulation)
        '''
        n = len(prices)
        m = 2

        dp = [[0] * m for _ in range(n+1)]

        for x in range(n-1,-1,-1):
            for y in range(m-1,-1,-1):

                if(y):
                    dp[x][y] = max(-prices[x] + dp[x+1][0], dp[x+1][1])
                else:
                    dp[x][y] = max(prices[x] + dp[x+1][1], dp[x+1][0])

        return dp[0][1]
        '''
        

        # space optimized
        n = len(prices)
        m = 2
        
        prevBuy = prevSell = 0
        
        for x in range(n-1,-1,-1):

            for y in range(m-1,-1,-1):

                if(y):
                    currBuy = max(
                        -prices[x] + prevSell,
                        prevBuy
                    )
                else:
                    currSell = max(
                        prices[x] + prevBuy,
                        prevSell
                    )
                
                prevSell = currSell
                prevBuy = currBuy
            
        
        return currBuy
        