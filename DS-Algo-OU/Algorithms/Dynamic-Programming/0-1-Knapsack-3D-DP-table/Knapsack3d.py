class DP3D():

    @staticmethod
    def solution(weights, volume, cost, weight_capacity, volume_capacity):

        k = len(weights) + 1
        l = weight_capacity + 1
        m = volume_capacity + 1

        dp = [[[0] * m for _ in range(l)] for _ in range(k)]

        # for x in dp:
        #     for y in x:
        #         print(y)
        #     print('----------------------------------------------------------------------',end='')
        #     print('')
        
        for x in range(1, k):
            for y in range(1, l): 
                for z in range(1, m):

                    if(weights[x-1] <= y and volume[x-1] <= z):
                        dp[x][y][z] = max(cost[x-1] + dp[x-1][y-weights[x-1]][z-volume[x-1]], dp[x-1][y][z])
                    else:
                        dp[x][y][z] = dp[x-1][y][z]


        # backtrack
        rem_weight = weight_capacity
        rem_volume = volume_capacity
        included_items = [0] * len(weights)

        for x in range(k-1, 0,-1):
            
            if(dp[x][rem_weight][rem_volume] != dp[x-1][rem_weight][rem_volume]):
                rem_weight -= weights[x-1]
                rem_volume -= volume[x-1]
                included_items[x-1] = 1
        
        ans = []
        for x in range(len(included_items)):
            
            if(included_items[x]):
                ans.append((weights[x],volume[x], cost[x]))
        
        return dp[-1][-1][-1], ans



if __name__ == '__main__':
    obj = DP3D()
    # obj.solution([1,2,3],[1,2,3],[1,2,3],2,3)
    obj.solution([1,2,3,4],[2,1,4,5],[10,8,12,15],5,6)