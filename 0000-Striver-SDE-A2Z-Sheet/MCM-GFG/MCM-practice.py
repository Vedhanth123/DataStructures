
class Solution:
    def matrixMultiplication(self, arr):

        def rec(i,j):

            if(i == j):
                return 0
            
            cost = float('inf')
            for k in range(i,j):

                cost = min(
                    cost, 
                    arr[i-1] * arr[k] * arr[j] + rec(i,k) + rec(k+1,j)
                )
            
            return cost

        answer = rec(1,len(arr)-1)
        print(answer)
    

Solution().matrixMultiplication(arr = [2, 1, 3, 4])

'''
[2, 1, 3, 4]
[2,1,3,4] -> 2,1,4 -> i-1, k, j

'''