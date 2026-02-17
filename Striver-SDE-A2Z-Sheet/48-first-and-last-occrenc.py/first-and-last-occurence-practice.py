from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # It will give me the first occurence
        def getFirstOccurence():

            left = 0
            right = len(nums) - 1
            answer = len(nums)

            while(left <= right):

                mid = left + (right - left) //2
                if(nums[mid] >= target):
                    right = mid - 1
                    answer = mid
                else:
                    left = mid + 1
            
       
            return -1 if(answer == len(nums) or nums[answer] != target) else answer
        
        def getLastOccurence():

            left = 0
            right = len(nums) - 1
            answer = 0
            while(left <= right):

                mid = left + (right - left) //2
                if(nums[mid] <= target):
                    left = mid + 1
                    answer = mid
                else:
                    right = mid - 1
            
       
            return answer
        
        first = getFirstOccurence()
        last = getLastOccurence()

        if(first == -1):
            return [-1,-1]
        else:
            return [first, last]

Solution().searchRange(nums = [5,7,7,8,8,10,10,10,10], target = 8)