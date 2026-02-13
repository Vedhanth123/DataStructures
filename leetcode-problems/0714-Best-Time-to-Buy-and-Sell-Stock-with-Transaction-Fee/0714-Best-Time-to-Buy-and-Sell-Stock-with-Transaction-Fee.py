class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
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
                    -prices[index] + rec(index + 1, 0),
                    rec(index + 1, 1)
                )
            else:
                profit = max(
                    prices[index] - fee + rec(index + 1, 1),
                    rec(index + 1, 0)
                )
            
            memo[(index, buy)] = profit
            return profit
        
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
                    dp[x][y] = max(
                        -prices[x] + dp[x+1][0],
                        rec(x+1,1)
                    )
                else:
                    dp[x][y] = max(
                        prices[x] - fee + dp[x+1][1],
                        rec(x+1,0)
                    )
        
        return dp[0][-1]
        '''

        # bottom up (space optimized)
        after = [0,0]
        n = len(prices)
        m = 2

        for x in range(n-1,-1,-1):
            for y in range(m-1,-1,-1):

                if(y):
                    after[1] = max(
                        -prices[x] + after[0],
                        after[1]
                    ) 
                else:
                    after[0] = max(
                        prices[x] - fee + after[1],
                        after[0]
                    )
        
        return after[1]
                