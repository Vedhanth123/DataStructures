# This problem is also a classic version of the partition dp.

# so.. the problem is we have to burst ballons and we will be rewarded based on the below condition
# if ith balloon is burst then reward = arr[i-1] * arr[i] * arr[i-1]

from typing import List

class Solution:

    def maxCoins(self, nums: List[int]) -> int:

        nums.insert(0,1)
        nums.append(1)

        print(nums)

        def rec(i,j):

            if(i == j):
                return nums[i]
            if(i > j):
                return 0
            
            cost = float('-inf')
            for x in range(i,j+1):

                cost = max(
                    cost, 
                    nums[x-1] * nums[x] * nums[x+1] + rec(i, x-1) + rec(x+1,j)
                )
            
            return cost

        answer = rec(1,len(nums)-1)
        print(answer)

Solution().maxCoins([3,1,5,8])

'''
nums = [3,1,5,8]

[3,1,5,8] -> [1]
[3,5,8] -> [3*1*5] -> 15

[3,5,8] -> [5]
[3,8] -> [3*5*8] -> 120

[3,8] -> [8]
[3] -> [3*8*1] -> 24

[3] -> [3]
[] -> [1*3*1] -> 3

15+120+24+3 => 162


'''