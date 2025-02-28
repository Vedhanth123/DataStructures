class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
    
        # First LCS problem cheyyali

        n = len(str1)
        m = len(str2)

        
        dp = [[0] * (m+1) for i in range(n+1)]

        
        for i in range(n):
            for j in range(m):

                if(str1[i] == str2[j]):
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])
        

        answer = ""

        # ippudu bottom up approach cheyyali
        i = n
        j = m

        while(i > 0 and j > 0):

                if(str1[i-1] == str2[j-1]):
                    answer += str1[i-1]
                    j -= 1
                    i -= 1

                else:
                    if(dp[i-1][j] > dp[i][j-1]):
                        answer += str1[i-1]
                        i -= 1
                    else:
                        answer += str2[j-1]
                        j -= 1
        
        while(j > 0):
            answer += str2[j-1]
            j -= 1
        
        while(i > 0):
            answer += str1[i-1]
            i -= 1
        
        return answer[::-1]



                    

