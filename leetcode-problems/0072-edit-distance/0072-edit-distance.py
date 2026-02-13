class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m = len(word2) + 1
        n = len(word1) + 1

        dp = [[0] * m for _ in range(n)]

        
        for x in range(n):
            dp[x][0] = x
        
        for x in range(m):
            dp[0][x] = x
        

        for x in range(1, n):
            for y in range(1, m):

                if(word1[x-1] == word2[y-1]):
                    dp[x][y] = dp[x-1][y-1]
                else:
                    dp[x][y] = 1 + min(dp[x-1][y-1], dp[x-1][y], dp[x][y-1])
        
        return dp[-1][-1]