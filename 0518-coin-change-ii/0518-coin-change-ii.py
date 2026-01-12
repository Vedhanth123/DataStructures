class Solution:
    def change(self, amount, coins) -> int:
        
        n = len(coins)
        m = amount

        dp = [[0] * (m+1) for _ in range(n+1)]

        for x in range(n+1):
            dp[x][-1] = 1

        for x in range(n-1,-1,-1):

            for y in range(m-1,-1,-1):

                if(y + coins[x] > m):
                    dp[x][y] = dp[x+1][y]
                else:
                    dp[x][y] = dp[x][y + coins[x]] + dp[x+1][y]
                
                if(x == 0 and y == 0):
                    print(dp[x][y], dp[x][y+coins[x]], dp[x+1][y])

        print('-' * 50)
        for row in dp:
            print(row)

        return dp[0][0]

Solution().change(10, [9,1])
