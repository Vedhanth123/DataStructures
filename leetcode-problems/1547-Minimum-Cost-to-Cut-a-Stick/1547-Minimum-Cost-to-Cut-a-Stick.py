from typing import List

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        # recursion + memoization
        '''
        def rec(left, right, cut_left, cut_right):

            # if there are no more cuts avaiable then return 0 (base case)
            if(cut_left >= cut_right):
                return 0
        
            min_cost = float('inf')
            for x in range(cut_left, cut_right):
                min_cost = min(
                    min_cost, 
                    right - left + rec(left, cuts[x], cut_left, x) + rec(cuts[x], right, x+1, cut_right)
                )
            return min_cost

        answer = rec(0,n, 0, len(cuts))  
        print(answer)
        '''

        # 2 parameter model
        cuts.sort()
        cuts.insert(0,0)
        cuts.append(n)

        def rec(i, j):

            if(i > j):
                return 0
            
            cost = float('inf')

            for x in range(i,j+1):
                cost = min(
                    cost, 
                    cuts[j+1] - cuts[i-1] + rec(i,x-1) + rec(x+1,j)
                )

            return cost

        answer = rec(1,len(cuts)-2)
        print(answer)



        # bottom up (tabulation)
        '''
        m = len(cuts)

        dp = [[float('inf')] * (m) for_ in range(m)]
        
        for x in range(n-1,-1,-1):

            for y in range(n-1,x-1,-1):

                dp[x][y] = 

        '''

Solution().minCost(n = 7, cuts = [1,3,4,5])

'''
[0,1,3,4,5,7] [1]
[0,1] [3,4,5,7] -> 7

[0,1] [3,4,5,7] -> [3]
[0,1] [3] [4,5,7] -> 4

[0,1] [3] [4,5,7] -> [4]
[0,1] [3] [4] [5,7] -> 3


'''

'''
1,2,3,4,5,6,7 [1] 
1 2,3,4,5,6,7 [1] -> 7

1 2,3,4,5,6,7 [3] -> 6
1 2,3 4,5,6,7 [3]

1 2,3 4,5,6,7 [4] 
1 2,3 4 5,6,7 [4] -> 4

1 2,3 4 5,6,7 [5] 
1 2,3 4 5 6,7 [5] -> 3


1,2,3,4,5,6,7 [3]
1,2,3 4,5,6,7 [3] -> 7

1,2,3 4,5,6,7 [1] 
1 2,3 4,5,6,7 [1] -> 3

1 2,3 4,5,6,7 [5]
1 2,3 4,5 6,7 [5] -> 4


'''