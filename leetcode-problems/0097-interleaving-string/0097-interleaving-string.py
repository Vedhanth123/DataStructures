class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        

        if(len(s1) + len(s2) != len(s3)):
            return False

        n = len(s1) + 1
        m = len(s2) + 1

        dp = [[0] * m for x in range(n)]

        dp[0][0] = True

        for x in range(1, n):
            dp[x][0] = (s1[x-1] == s3[x-1] and dp[x-1][0])
        
        for x in range(1, m):
            dp[0][x] = (s2[x-1] == s3[x-1] and dp[0][x-1])
        
        for x in range(1, n):

            for y in range(1, m):

                dp[x][y] = (s1[x-1] == s3[x+y-1] and dp[x-1][y]) or (s2[y-1] == s3[x+y-1] and dp[x][y-1])
        
        return dp[-1][-1]
        