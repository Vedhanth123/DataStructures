class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:


        dp = [cost[0], cost[1]] + [0] * (len(cost) - 2)

        for x in range(2, len(dp)):
            dp[x] = cost[x] + min(dp[x-1], dp[x-2])
        
        return min(dp[-1],dp[-2])