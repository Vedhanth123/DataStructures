from typing import List

# This problem has a unique twist when compared to "best time to buy and sell stock 2"
# The problem here is that we can only make 2 such transactions

# to solve this we've used counter whenever we buy and sell. Meaning each buy is a half transaction and when the sell is made after the stock is bought then the transaction is completed. 
# If we reach our transaction count then we cannot make any other transactions (meaning our cecision will tree will be completed over here leaving us to stop our recursion)

# how do we solve this problem. simple! we create another parameter to carry our transaction count to the down layers in our recursion. meaning we are sending the parameters to our lower trees

# but... to solve this exact problem in tabluation method, we need to take care about the parameters (3 in this case)
# base cases.... if base cases are considered. (remember our base case for stopping the transactions because to completion of transaction chances is 0 or we could reverse it)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # recursion + memoization

        '''
        n = len(prices)

        memo = {}

        def rec(index, buy, count):

            if((index, buy, count) in memo):
                return memo[(index, buy,count)]

            if(count == 4 or index == n):
                return 0
            
            profit = 0

            if(buy):
                profit = max(
                    -prices[index] + rec(index + 1, 0, count + 1),
                    rec(index + 1, 1, count)
                )
            else:
                profit = max(
                    prices[index] + rec(index + 1, 1, count + 1),
                    rec(index + 1, 0, count)
                ) 
            
            memo[(index, buy, count)] = profit
            return profit
        
        return rec(0,1,0)
        '''


        # bottom up (tabulation)
        '''
        n = len(prices)
        m = 2
        o = 4
        dp = [[[0] * (o+1) for _ in range(m)] for _ in range(n+1)]

        for x in range(n-1,-1,-1):

            for y in range(m-1,-1,-1):

                for z in range(o-1,-1,-1):

                    if(y == 0):
                        dp[x][y][z] = max(
                            prices[x] + dp[x+1][1][z+1],
                            dp[x+1][0][z]
                        )
                    else:
                        dp[x][y][z] = max(
                            -prices[x] + dp[x+1][0][z + 1],
                            dp[x+1][1][z]
                        )

        return dp[0][1][0]
        '''
        
        # bottom up (space optimzized)
        n = len(prices)
        m = 2
        o = 4

        after = [[0] * (o+1) for _ in range(m)]

        for x in range(n-1,-1,-1):

            for y in range(m-1,-1,-1):

                for z in range(o-1,-1,-1):

                    if(y == 1):
                        after[1][z] = max(
                            -prices[x] + after[0][z+1],
                            after[1][z]
                            )
                    else:
                        after[0][z] = max(
                            prices[x] + after[1][z+1],
                            after[0][z]
                        )

        return after[1][0]


print(Solution().maxProfit(prices = [3,3,5,0,0,3,1,4]))