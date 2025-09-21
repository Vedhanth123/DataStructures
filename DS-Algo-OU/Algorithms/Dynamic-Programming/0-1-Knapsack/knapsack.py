class Knapsack():

    @staticmethod
    def calculate(weight, profit, capacity):

        # I need to find the combination of items where there is high profit within the capacity of the bag

        # I will use DP for it
        m = capacity + 1
        n = len(weight) + 1

        dp = [[0] * m for _ in range(n)]

        
        # I will have two choices.
        # 1) If I don't chose the ith item what would be the profit
        # 2) If I choose ith them what would be the profit
        # 3) so.... dp[i][j] = max(dp[i-1][j], profit[i-1] + dp[i-1][j-weight[i-1]])

        # let's try this and check what would our recurrence relation would be

        for x in range(1,n):            
            for y in range(1, m):
                if(weight[x-1] <= y):
                    dp[x][y] = max(dp[x-1][y], profit[x-1] + dp[x-1][y-weight[x-1]])
                else:
                    dp[x][y] = dp[x-1][y]
        
        # for row in dp:
        #     print(row)

        # Now I need to backtrack

        # The approach is that I start from the bottom right cell of dp table
        # I will check the cell which is right above this. 
        # This means that if this cell's value is different from the cell which is above then it
        # means that the current items is selected. 
        # THe further backtracking can be done by changing the column too..
        # so.. 
        # if(dp[i-1][j] != dp[i][j]) -> If the item is included
        #   included[1] = 1
        #   j -= weight[i]
        # else:
        #    j -= 1
        
        included = [0] * (n-1)

        i = n-1
        j = m-1

        while i > 0 and j > 0:

            if(dp[i-1][j] != dp[i][j]):
                included[i-1] = 1
                j -= weight[i-1]

            i -= 1

        ans = []
        for x in range(n-1):
            if(included[x]):
                ans.append((weight[x],profit[x]))
        
        return ans


if __name__ == '__main__':
    obj = Knapsack()
    obj.calculate([2,4,6],[10,30,20], 14)