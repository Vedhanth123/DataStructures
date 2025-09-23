class Knapsack():

    @staticmethod
    def calculate(weights, cost, capacity):

        m = capacity + 1
        n = len(weights) + 1

        dp = [[0] * m for _ in range(n)]

        for x in range(1,n):
            for y in range(1, m):

                if(weights[x-1] <= y):
                    dp[x][y] = max(dp[x-1][y], dp[x-1][y-weights[x-1]] + cost[x-1])
                else:
                    dp[x][y] = dp[x-1][y]
        
        
        # backtracking
        included = [0] * len(weights)
        rem_capacity = m-1
        for x in range(n-1,0,-1):

            if(dp[x][rem_capacity] != dp[x-1][rem_capacity]):
                rem_capacity -= weights[x-1]
                included[x-1] = 1
        
        ans = []
        for x in range(len(included)):
            if(included[x] == 1):
                ans.append((weights[x],cost[x]))
        
        return ans

if __name__ == '__main__':
    obj = Knapsack()
    obj.solution([1,2,3],[20,30,10],5)