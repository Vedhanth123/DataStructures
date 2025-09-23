class knapsack():

    @staticmethod
    def solution(weights, values, capacity):

        n = len(weights)
        m = capacity + 1

        dp = [0] * m

        for x in range(1,m):
            for y in range(n):

                if(weights[y] <= x):
                    dp[x] = max(dp[x], values[y] + dp[x-weights[y]])
                else:
                    dp[x] = max(dp[x-1], dp[x])
        

if __name__ == '__main__':
    obj = knapsack()
    obj.solution([1,3,4],[15,40,50],7)
