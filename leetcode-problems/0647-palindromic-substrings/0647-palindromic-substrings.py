class Solution:
    def countSubstrings(self, s: str) -> int:

        n = len(s)

        dp = [[False] * n for x in range(n)]

        count = 0
        for gap in range(n):

            for i in range(n-gap):

                j = i + gap
                
                if(gap == 0):
                    dp[i][j] = True
                
                if(gap == 1 and s[i] == s[j]):
                    dp[i][j] = True
                
                if(gap >= 2 and s[i] == s[j] and dp[i+1][j-1]):
                    dp[i][j] = True


                if(dp[i][j]):
                    count += 1
        
        return count
        
                    
                    
