class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        

        dp = [cost[0], cost[1]] + [-1] * (len(cost) - 2)

        for x in range(2, len(cost)):
            dp[x] = cost[x] + min(dp[x-1], dp[x-2])
        
        return min(dp[-2:])