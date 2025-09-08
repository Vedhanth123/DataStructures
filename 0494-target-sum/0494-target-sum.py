class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        

        if(target > sum(nums) or target < -sum(nums)):
            return 0

        n = len(nums)
        m = (sum(nums)+1)*2

        dp = [[0] * (m+1) for _ in range(n+1)]
        dp[0][m//2] = 1
    
        for x in range(n):
            for y in range(m):

                if(dp[x][y] > 0):
                    dp[x+1][y+nums[x]] += dp[x][y]
                    dp[x+1][y-nums[x]] += dp[x][y]
        
        return dp[-1][(m//2) + target]