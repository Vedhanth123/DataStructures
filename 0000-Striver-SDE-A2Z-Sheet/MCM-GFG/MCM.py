# MCM problem is an example problem of optimization of multiplications using partition DP.

# in simple words. a series of matrices are given and we need to partition them such that multiplying the partitions give us the minimum multiplcation steps as possible

# for example [10,30,5, 60]

# the above diagram shows the dimensions of the matrices
# we usually have n-1 matrices n=4 so 3 matrices => matrix A = 10x30, matrix B 30x5, matrix C 5x60

# we could multiple (AB)C or A(BC) we only need to find the best way to multiply such that we take minimal number of steps to multiply them.

# so... the basic thing is to run a loop and start partitioning them. We solve the left part and right part.
# for iterating we use k
# for taking care of the boundaries of the left part and right part we use i,j

# also we find the actual cost of muliplying the matrix by arr[i-1] * arr[k] * arr[j] (left and middle and right)
# we call the function once again so that they are computed again.


class Solution:
    def matrixMultiplication(self, arr):

        # recurion + (memoization)
        # code here
        '''
        memo = {}
        def rec(i, j):
            
            if((i,j) in memo):
                return memo[(i,j)]
            
            if(i == j):
                return 0
            
            mini = float('inf')
            
            for k in range(i,j):
                mini = min(mini, arr[i-1]*arr[k]*arr[j] + rec(i,k) + rec(k+1, j))
            
            memo[(i,j)] = mini
            return mini
        
        return rec(1,len(arr)-1)
        '''

        # bottom up (tabulation)

        n = len(arr)
        dp = [[float('inf')] * (n) for _ in range(n)]

        for x in range(n):
            dp[x][x] = 0
        
        for x in range(n-1,0,-1):

            for y in range(x+1,n):

                for z in range(x,y):
                    dp[x][y] = min(
                        dp[x][y], 
                        arr[x-1]*arr[z]*arr[y] + dp[x][z] + dp[z+1][y]
                    )
        
        for row in dp:
            print(row)
        return dp[1][-1]



Solution().matrixMultiplication([10, 30, 5, 60])
# Solution().matrixMultiplication([2,1,3,4])