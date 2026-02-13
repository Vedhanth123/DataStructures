class Solution:
    def findTargetSumWays(self, nums, target):
        
        '''
        memo = {}

        def helper(index, total):

            if((index, total) in memo):
                return memo[(index,total)]
            
            if(index >= len(nums) and total == target):
                return 1
            elif(index >= len(nums) and total != target):
                return 0
            
            memo[(index, total)] = helper(index + 1, total + nums[index]) + helper(index + 1, total - nums[index])
            return memo[(index, total)]

        
        return helper(0,0)
        '''
        n = len(nums)
        
        m = (2*target)

        dp = [[0] * (m+1) for _ in range(n+1)]
    
        dp[-1][target+target] = 1
    
        for row in dp:
            print(row)
        
        for x in range(n-1,-1,-1):
            for y in range(m-1,-1,-1):

                if(y + nums[x] > m):
                    dp[x][y] = dp[x+1][y-nums[x]]
                if(y - nums[x] < 0):
                    dp[x][y] = dp[x+1][y+nums[x]]
                
                if(y + nums[x] <= m and y - nums[x] >= 0):
                    dp[x][y] = dp[x+1][y + nums[x]] + dp[x+1][y - nums[x]]
        
        print('-' * 100)
        for row in dp:
            print(row)

Solution().findTargetSumWays(nums = [1,1,1,1,1], target = 3)

