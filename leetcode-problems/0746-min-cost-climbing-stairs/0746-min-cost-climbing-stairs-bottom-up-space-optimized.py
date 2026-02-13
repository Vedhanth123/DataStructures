class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        prev2 = cost[0]
        prev1 = cost[1]

        for x in range(2, len(cost)):

            curr = cost[x] + min(prev1, prev2)
            prev2 = prev1
            prev1 = curr
        
        return min(prev2, prev1)