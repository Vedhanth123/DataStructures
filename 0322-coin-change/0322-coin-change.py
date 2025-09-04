class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float('inf')] * (amount+1)

        dp[0] = 0

        for x in range(1, amount+1):

            for coin in coins:

                if(coin <= x):
                    dp[x] = min(dp[x], dp[x-coin] + 1)
        
        return dp[-1] if dp[-1] != float('inf') else -1
            
                    