from os import *
from sys import *
from collections import *
from math import *

from sys import stdin

def maximumNonAdjacentSum(nums):    
    # Write your code here.

    # recursion + memoization
    '''
    memo = [-1] * len(nums)

    def rec(x):

        if(x >= len(nums)):
            return 0

        if(memo[x] != -1):
            return memo[x]
        
        memo[x] = max(nums[x] + rec(x+2), rec(x+1))
        return memo[x]
    
    return rec(0)

    '''
    # bottom up (tabulation)
    '''
    n = len(nums)

    dp = [-1] * len(nums) + [0,0]

    for x in range(n-1,-1,-1):

        dp[x] = max(nums[x] + dp[x+2], dp[x+1])
    
    return dp[0]
    '''

    # bottom up + space optimized
    plus1 = plus2 = 0

    for x in range(n-1,-1,-1):
        curr = max(nums[x] + plus2, plus1)
        plus2 = plus1
        plus1 = curr

    return plus1

# Main.
t = int(stdin.readline().rstrip())

while t > 0:
    
    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    print(maximumNonAdjacentSum(arr))
    
    t -= 1