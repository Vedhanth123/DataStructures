from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        
        smallestIndex = 0
        smallestValue = nums[0]

        for x in range(len(nums)):
            
            if(smallestValue > nums[x]):
                smallestValue = nums[x]
                smallestIndex = x
        
        for x in range(smallestIndex, smallestIndex + len(nums)-1):

            if(nums[x%len(nums)] > nums[(x+1)%len(nums)]):
                return False
        
        return True
            
obj = Solution()
obj.check([3,4,5,1,2])