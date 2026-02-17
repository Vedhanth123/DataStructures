from typing import List
class Solution:    
    def singleNonDuplicate(self, nums: List[int]) -> int:

        left = 0
        n = len(nums)
        right = n- 1
        
        while(left <= right):

            mid = left + (right - left) // 2
            noOfElements = ((right - left) + 2) // 2
            if(mid-1 >= 0 and mid+1 < n and 
               (nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1])):
                return nums[mid]
            elif(noOfElements % 2 and 
               (mid-1 >= 0 and nums[mid] == nums[mid-1])):
                right = mid - 2
            elif(noOfElements % 2 and 
               (mid+1 < n and nums[mid] == nums[mid+1])):
                left = mid + 2
            elif(noOfElements % 2 == 0 and 
               (mid+1 < n and nums[mid] == nums[mid+1])):
                right = mid - 1
            elif(noOfElements % 2 == 0 and 
                (mid-1 >= 0 and nums[mid] == nums[mid-1])):
                left = mid + 1

print(Solution().singleNonDuplicate(nums = [1,1,2,3,3,4,4,8,8]))