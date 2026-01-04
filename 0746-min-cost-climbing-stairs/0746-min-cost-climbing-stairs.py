class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {}
        def rec(n):

            if(n in memo):
                return memo[n]

            if(n == len(cost)):
                return 0
            
            # 1 step
            oneStep = cost[n] + rec(n+1)
            if(n < len(cost)-1):
                twoStep = cost[n+1] + rec(n+2)
            else:
                twoStep = 0
            memo[n] = min(oneStep, twoStep)
            return memo[n]
        
        return rec(0)