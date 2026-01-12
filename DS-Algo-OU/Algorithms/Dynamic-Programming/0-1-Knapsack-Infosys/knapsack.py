class Knapsack():

    def solution(self, weights, value, capacity):

        n = len(weights) + 1
        m = capacity + 1

        dp = [[0] * m for x in range(n)]

        # fill in the knapsack
        for x in range(1, n):
            for y in range(1, m):

                if(weights[x-1] <= y):
                    dp[x][y] = max(dp[x-1][y], dp[x-1][y-weights[x-1]] + value[x-1])
                else:
                    dp[x][y] = dp[x-1][y]
        
        items = [[]]
        w = m-1
        for x in range(n-1,0,-1):
            if(dp[x-1][w] != dp[x][w]):
                items[0].append((x, value[x-1]))
                w -= weights[x-1]
        
        print(items)
        return dp[-1][-1], items
            
