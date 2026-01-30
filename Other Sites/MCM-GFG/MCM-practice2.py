# I just wanted to practice this concept once again so that it will fit in my brain once and for all
# so... This problem is a textbook problem (standard problem) whichs builds upon a new concept called partiion DP

# Partition DP is a concept in which we make many partitions
# and find out which partition is best for our purpose
# Coming to this exact problem
# We are given a task of multiplying a sequence of matrices
# As we all know that matrix multiplication is a heafty business
# Also matrices can be multiplied in any order
# for example if (A,B,C,D) are matrices

# You have multiple choices to multiply them
# (AB)(CD) or (ABC)D or A(BC)(D) or many more options

# Why do we do that... let's say that cost of multiplication of AB and BC is different
# so.... naturally we will find a way to multiply all of them using the minimum cost as possible.

# you can find more about this concept in strivers video.
# https://www.youtube.com/watch?v=vRVfmbCFW7Y&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=49&pp=iAQB

# let's start our process...


# so... we are given a list of which contains the dimenensions of the matrices
# there are n-1 matrices in the list and our responsibility is to find out the best partition possible which helps us to multiply all of them with least cost as possible

#    A B C
# [2,1,3,4]

# so.. the problem goes by
# 

# we could try multiple approaches in multiplying them
# the main this is that we can't multiply a single matrix we need atleast 2 matrices (base case)
# Also you can multiply A*B but not B*A meaning left <= right (always!)

# so... initially i will be at 1 and j will be at the last index 
# (both the pointers will be at the last index) (Vedhanth's observation)

# let's dry run the the solution
# [2,1,3,4]
     
'''
   i   j  (i=1, j=3)
[2,1,3,4]

I will call this function

[2,1,3,4] (I will try to partiion in the below following)

[2][1,3,4] (i=1,k=1,j=3) splits would be (f(i,k),f(k+1,j)) f(1,1),f(2,3)
[2,1][3,4] (i=1,k=2,j=3) splits would be (f(i,k),f(k+1,j)) f(1,2),f(3,3)
[2,1,3][4] (i=1,k=3,j=3) splits would be (f(i,k),f(k+1,j)) f(1,3),f(4,3)

so... f(1,1) and f(4,3) will not be working as there is only 1 thing to do and not possible
so... coming to f(2,3) -->>
[1,3,4] (i=2,k=2,j=3)

[1][3,4] (i=2,k=2,j=3) splits would be (f(i,k),f(k+1,j)) f(2,2),f(3,3)

now about f(1,3)
[2,1,3] (i=1,k=1,j=3)
(i=1,k=1,j=3) splits would be f(i,k),f(k+1,j) f(1,1),f(2,3)
(i=1,k=2,j=3) splits would be f(i,k),f(k+1,j) f(1,2),f(3,3)


so... pseudocode will be
for k in range(i, j):

and about the multiplication part
arr[i-1] * arr[k] * arr[j]


'''

class Solution:
    def matrixMultiplication(self, arr):

        # recursion
        '''
        def rec(i,j):

            if(i >= j):
                return 0
        
            cost = float('inf')
            for k in range(i,j):

                cost = min(
                    cost,
                    arr[i-1] * arr[k] * arr[j] + rec(i,k) + rec(k+1,j)
                )
            
            return cost
        
        return rec(1,len(arr)-1)
        '''

        # bottom up
        '''
        '''

        n = len(arr)

        dp = [[float('inf')] * (n+1) for _ in range(n+1)]

        for x in range(n+1):
            dp[x][x] = 0

        for row in dp:
            print(row)        

        
        for x in range(n-1,0,-1):

            for y in range():

                for k in range(y-1,x-1,-1):
                    dp[x][y] = min(
                        dp[x][y],
                        arr[x-1] * arr[]
                    )


Solution().matrixMultiplication([2,1,3,4])


