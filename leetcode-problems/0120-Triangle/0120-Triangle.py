from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        # top down recursion + memoization
        '''

        memo = {}

        def rec(row, col):

            if((row,col) in memo):
                return memo[(row,col)]
            
            if(row == len(triangle)):
                return 0
            if(col >= len(triangle[row])):
                return float('inf')
            
            memo[(row,col)] = triangle[row][col] + min(rec(row+1, col), rec(row+1, col+1))
            return memo[(row,col)]
        
        return rec(0,0)
    
        '''
        
        # Bottom up tabulation method
        '''

        dp = []
        n = len(triangle)

        for x in range(n+1):
            dp.append([0] * (x+1))
        

        for row in dp:
            print(row)

        for x in range(n-1,-1,-1):
            for y in range(x,-1,-1):
                
                dp[x][y] = triangle[x][y] + min(dp[x+1][y],dp[x+1][y+1])
    
        print(dp[0][0])

        '''
        # bottom up + space optmization

        # in order to optimize the space of the tabulation method.
        # we've observed that we only need two adjacent rows
        # soo... if I start from the bottom of the table
        # I first need n+1th size array 
        # I then need nth size array
        # the same process continues
        
        n = len(triangle)

        prev = [0] * (n+1)

        for x in range(n-1,-1,-1):

            curr = [0] * (x+1)
            for y in range(x,-1,-1):

                curr[y] = triangle[x][y] + min(prev[y],prev[y+1])
            
            prev = curr
        
        return curr[0]

print(Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))