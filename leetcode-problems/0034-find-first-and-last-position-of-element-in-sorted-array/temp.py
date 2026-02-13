from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # 1) First find the target value in the array.
        # 2) If the target value is found in the array
        # 3) Check for the first occurence of the target value in the array
        # 4) To check for the first occurence of the target value in the array. Check if the value at the mid-1 
        # is equal to the target value. If it is then the first occruence of the target value must lie between left
        # mid - 1. Move the right to mid - 1 and check till the condition breaks
        # if not then mid - 1 is the first occurence of the target value
        # 5) To find the last occurence of the target value do the same thing you did to find for the first occurence 
        # of the target value

        left = 0
        right = len(nums)
        
        answer = [-1,-1]

        while(left < right):            
            mid = (left + right) // 2

            if(nums[mid] == target):
                # serach for the first occruence of the target value
                if(mid == 0 or nums[mid-1] != target):
                    answer[0] = mid
                    break
                else:
                    right = mid
                    
            elif(target > nums[mid]):
                left = mid + 1
            else:
                right = mid
            
        left = 0
        right = len(nums)

        while(left < right):            
            mid = (left + right) // 2

            if(nums[mid] == target):
                # serach for the first occruence of the target value
                if(mid == len(nums)- 1 or nums[mid+1] != target):
                    answer[1] = mid
                    break
                else:
                    left = mid + 1

            elif(target > nums[mid]):
                left = mid + 1
            else:
                right = mid
            
        return answer

Solution().searchRange([2,2], 2)