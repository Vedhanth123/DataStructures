from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        # recursion + memo
        '''
        n = len(matrix)

        memo = {}

        def rec(x,y):
            
            if((x,y) in memo):
                return memo[(x,y)]
            
            if(x == n):
                return 0
            
            if(y < 0 or y == n):
                return float('inf')
            
            memo[(x,y)] = matrix[x][y] + min(rec(x+1,y-1), rec(x+1, y), rec(x+1,y+1))
            return memo[(x,y)]

        answer = float('inf')
        for x in range(n):

            answer = min(answer, rec(0,x))
        
        return answer
        '''
        # bottom up 
    
        '''
        n = len(matrix)

        dp = [[0] * (n) for _ in range(n+1)]

        for x in range(n-1,-1,-1):
            for y in range(n-1,-1,-1):
                
                left,down,right = (float('inf'),float('inf'),float('inf'))

                if(y-1 >= 0):
                    left = dp[x+1][y-1]
                if(y+1 < n):
                    right = dp[x+1][y+1]
                down = dp[x+1][y]

                dp[x][y] = matrix[x][y] + min(left, down,right)
    
  
        return min(dp[0])
    
        '''
        # bottom up + space optimized
        n = len(matrix)
        curr = [0] * n

        for x in range(n-1,-1,-1):
            prev = [0] * n
            for y in range(n-1,-1,-1):

                left, down, right = (float('inf'), float('inf'), float('inf'))

                if(y-1 >= 0):
                    left = prev[y-1]
                if(y+1 < n):
                    right = prev[y+1]
                down = prev[y]

                curr[y] = matrix[x][y] + min(left, down, right)
            
            prev = curr
        
        return min(curr)
    
    
print(Solution().minFallingPathSum([[100,-42,-46,-41],[31,97,10,-10],[-58,-51,82,89],[51,81,69,-51]]))

'''
[100, -42, -46, -41]
[31 , 97, 10, -10]
[-58, -51, 82, 89]
[51 , 81, 69, -51]
'''