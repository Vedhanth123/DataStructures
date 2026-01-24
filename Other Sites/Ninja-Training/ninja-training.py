from typing import *

  
def ninjaTraining(n: int, points: List[List[int]]) -> int:

    # recursion + memoization
    '''
    m = len(points[0])

    memo = [[0] * m for _ in range(n+1)]

    def rec(x, skipper):

        if(memo[x][skipper] != 0):
            return memo[x][skipper]

        if(x == n):
            return 0
        
        ans = 0
        for y in range(len(points[x])):
            if(y != skipper):
                ans = max(ans, points[x][y] + rec(x+1, y))
        
        memo[x][skipper] = ans
        return memo[x][skipper]
    
    return max(rec(0,0), rec(0,1), rec(0,2))
    '''

    # bottom up (tabulation)
    m = len(points)

    dp = [[0] * m for _ in range(n+1)]

    for x in range(n-1,-1,-1):

        for y in range(m-1,-1,-1):

            answer = 0
            for z in range(m-1,-1,-1):
                if(z != y):
                    answer = max(answer, points[x][y] + dp[x+1][z])
            
            dp[x][y] = answer
    
    return (dp[0])

ninjaTraining(3, [[1,2,5],[3,1,1],[3,3,3]])


            


            
