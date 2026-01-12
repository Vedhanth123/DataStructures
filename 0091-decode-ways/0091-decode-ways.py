class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = [1] + [0] * len(s)

        for x in range(1,len(s)+1):

            if(int(s[x-1]) != 0):
                dp[x] = dp[x-1]

            if(x-2 >= 0 and int(s[x-2]) == 1):
                dp[x] += dp[x-2]
            elif(x-2 >= 0 and int(s[x-2]) == 2 and int(s[x-1]) <= 6):
                dp[x] += dp[x-2]
        
        return dp[-1]
