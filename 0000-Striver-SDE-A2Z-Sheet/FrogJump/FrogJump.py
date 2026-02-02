class Solution:
    def minCost(self, height):
        # code here
        
        # forward recursion
        '''
        answer = [float('inf')]
        def rec(x, travellingSum):
            
            if(x == len(height) -1 ):
                answer[0] = min(answer[0], travellingSum)
                return
        
            if(x+1 < len(height)):
                rec(x+1, travellingSum + abs(height[x] - height[x+1]))
            if(x+2 < len(height)):
                rec(x+2, travellingSum + abs(height[x] - height[x+2]))
        
        rec(0,0)
        return answer[-1]
        '''

        # reverse recursion
        '''
        memo = [float('inf')] * len(height)

        def rec(x):
            
            if(memo[x] != float('inf')):
                return memo[x]
            
            if(x >= len(height)):
                return float('inf')
            
            if(x == len(height)-1):
                return 0
            
            oneStep = twoStep = float('inf')
            if(x+1 < len(height)):
                oneStep = abs(height[x] - height[x+1]) + rec(x+1)
            if(x+2 < len(height)):
                twoStep = abs(height[x] - height[x+2]) + rec(x+2)
            
            memo[x] = min(oneStep, twoStep)
            return memo[x]
    
        return rec(0)
        '''

        # bottom up (tabulation)
        '''
        n = len(height)

        if(n <= 1):
            return 0
        if(n >= 2):
            dp = [float('inf')] * (n-2) + [abs(height[-1]-height[-2]), 0]

            for x in range(n-3,-1,-1):
                
                dp[x] = min(
                    height[x] - height[x+1] + dp[x+1],
                    height[x] - height[x+2] + dp[x+2]
                )
            
            return dp[0]
        '''
    
        # bottom up tabulation + space optmized

        n = len(height)
        if(n <= 1):
            return 0
        if(n > 1):

            oneStep = height[-2]
            twoStep = 0

            for x in range(n-3,-1,-1):

                curr = min(
                    abs(height[x] - height[x+1]) + oneStep,
                    abs(height[x] - height[x+2]) + twoStep
                )
                twoStep = oneStep
                oneStep = curr
            
            return curr


Solution().minCost([10, 30, 40, 20, 50])