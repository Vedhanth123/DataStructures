class Solution:
    def isSubsetSum (self, arr, sum):
        # code here 
        
        # recursion
        '''
        n = len(arr)

        def rec(index, curr_sum):
            
            if(index == n or curr_sum > sum):
                return False

            if(curr_sum == sum):
                return True

            return rec(index+1, curr_sum+arr[index]) or rec(index+1, curr_sum)
        
        return rec(0,0)
        '''

        # bottom up (tabulation)
        n = len(arr)
        m = sum
        dp = [[False] * (m+1) for _ in range(n+1)]
        
        for x in range(n+1):
            dp[x][-1] = True

        for x in range(n-1,-1,-1):

            for y in range(m-1,-1,-1):
                
                if(y + arr[x] <= m):
                    dp[x][y] = dp[x+1][y + arr[x]] or dp[x+1][y]
                else:
                    dp[x][y] = dp[x+1][y]
        return dp[0][0]



print(Solution().isSubsetSum([3, 34, 4, 12, 5, 2], sum = 9))


