
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        answer = []
        for x in range(len(nums)-2):

            left = x+1
            right = len(nums) - 1
            val = nums[x]
            while(left < right):

                sum_ = nums[left] + nums[right]
                if(val + sum_ == 0):
                    answer.append([val, nums[left], nums[right]])
                    left += 1
                elif(val + sum_ < 0):
                    left += 1
                else:
                    right -= 1
        
        return answer
    
obj = Solution()
obj.threeSum(nums = [-1,0,1,2,-1,-4])