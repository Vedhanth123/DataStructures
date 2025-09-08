class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        m = amount + 1
        n = len(coins) + 1
        dp = [[0] *m for x in range(n)]

        for x in range(n):
            dp[x][0] = 1
        
        for x in range(1, n):
            for y in range(1,m):

                if(coins[x-1] <= y):

                    dp[x][y] = dp[x-1][y] + dp[x][y - coins[x-1]]
                else:
                    dp[x][y] = dp[x-1][y]
        
        for row in dp:
            print(row)
        return dp[-1][-1]
        