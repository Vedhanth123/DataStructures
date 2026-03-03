class Solution:

    def knapsack(self, W, val, wt):
        # code here

        # pure recursion

        '''
        def rec(index, curr_weight):

            if(index == len(val)):
                return 0
        
            take = not_take = 0
            if(curr_weight + wt[index] <= W):
                take = val[index] + rec(index + 1, curr_weight + wt[index])
            not_take = rec(index + 1, curr_weight)
        
            return max(take, not_take)

        return rec(0,0)
        '''

        # recursion + memoization
        
        '''
        n = len(val)
        m = W
        memo = [[0] * (m+1) for _ in range(n)]

        def rec(index, curr_weight):
        
            if(index == n):
                return 0

            if(memo[index][curr_weight] != 0):
                print("I am being called")
                return memo[index][curr_weight]
        
            if(curr_weight + wt[index] <= W):
                take = val[index] + rec(index + 1, curr_weight + wt[index])
            else:
                take = 0
            not_take = rec(index + 1, curr_weight)
        
            memo[index][curr_weight] = max(take, not_take)
        
            return memo[index][curr_weight]
        
        return rec(0,0)
        '''
        

        # bottom up (tabulation)

        n = len(val)
        m = W
        dp = [[0] * (m+1) for _ in range(n+1)]

        for x in range(n-1,-1,-1):
            for y in range(m-1,-1,-1):

                if(y + wt[x] <= m):
                    dp[x][y] = max(val[x] + dp[x+1][y + wt[x]], dp[x+1][y])
                else:
                    dp[x][y] = dp[x+1][y]
        
        return dp[0][0]
    



print(Solution().knapsack(4, [6 ,3 ,8, 6, 9 ,8, 2, 4 ,10 ,9],[2 ,1, 3 ,1, 4, 1, 2, 2 ,5 ,7]))

