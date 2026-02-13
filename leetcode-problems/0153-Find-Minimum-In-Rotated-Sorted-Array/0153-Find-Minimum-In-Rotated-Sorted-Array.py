from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums)

        while(left < right):

            if(left == right - 2):
                return min(nums[left], nums[right-1])

            mid = (left + right) // 2

            if(nums[right-1] <= nums[mid]):
                left = mid + 1
            elif(nums[mid] >= nums[left]):
                right = mid

Solution().findMin(nums = [3,4,5,1,2])