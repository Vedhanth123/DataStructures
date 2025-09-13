class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if(sum(nums) % 2):
            return False
        
        m = sum(nums) // 2
        n = len(nums)
        dp = [[False] * (m + 1) for x in range(n + 1)]

        for x in range(n+1):
            dp[x][0] = True

        for x in range(1, n+1):
            for y in range(1, m+1):

                if(nums[x-1] <= y):
                    if(dp[x-1][y-nums[x-1]] == True):
                        dp[x][y] = True
                    else:
                        dp[x][y] = dp[x-1][y]
                else:
                    dp[x][y] = dp[x-1][y]

        
        # for row in dp:
        #     print(row)
        ans = False
        for x in range(1,n+1):
            ans = ans or dp[x][-1]

        return ans
