class Solution:
    def numDecodings(self, s: str) -> int:
        
        memo = {}

        def rec(x):

            if(x in memo):
                return memo[x]
            if(x >= len(s)):
                return 1
            
            if(int(s[x]) == 0):
                memo[x] = 0
                return memo[x]

            if(int(s[x]) == 1 and x+1 < len(s)):
                memo[x] = rec(x + 2) + rec(x + 1)
                return memo[x]
            if(int(s[x]) == 2 and x+1 < len(s) and int(s[x+1]) <= 6):
                memo[x] = rec(x + 2) + rec(x + 1)
                return memo[x]
            else:
                memo[x] = rec(x+1)
                return memo[x]

        return rec(0)

            

            
