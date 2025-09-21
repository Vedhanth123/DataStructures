from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        
        left = 0
        right = len(nums)

        while(left < right):

            mid = left + (right - left) // 2

            if(nums[mid] <= target):
                right = mid
            else:
                left = mid + 1
        
obj = Solution()

obj.searchRange([5,7,7,8,8,10], target = 8)