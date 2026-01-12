

class Solution:
    def canPartition(self, nums):
        
        sum_ = sum(nums)

        if(sum_ % 2):
            return False
        
        m = sum_ // 2
        n = len(nums)

        dp = [[False] * (m+1) for _ in range(n+1)]

        for x in range(n+1):
            dp[x][-1] = True
        
        for x in range(0,m+1):
            print(f"  {x} ", end="")
        print("")
        for row in dp:
            print(row)

        for x in range(n-1,-1,-1):

            for y in range(m-1,-1,-1):

                if(y + nums[x] > m):
                    dp[x][y] = dp[x+1][y]
                
                else:
                    dp[x][y] = dp[x+1][y] or dp[x+1][y+nums[x]]
        
        for row in dp:
            print(row)

Solution().canPartition([1,5,11,5])