class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        if(m == 1 and n == 1):
            return 1

        dp = [[0] * n for x in range(m)]

        for x in range(m):
            dp[x][0] = 1
        
        for y in range(n):
            dp[0][y] = 1

        dp[0][0] = 0

        for x in range(1,m):
            for y in range(1,n):

                dp[x][y] += dp[x-1][y] + dp[x][y-1]
        
        return dp[-1][-1]