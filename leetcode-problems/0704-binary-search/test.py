from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while(left <= right):

            mid = left + (right - left) // 2
            if(target == nums[mid]):
                return mid
            elif(target < nums[mid]):
                right = mid
            else:
                left = mid + 1

        return -1    
    
obj = Solution()

nums = [-1,0,3,5,9,12]
obj.search(nums, 12)
target = 9

for target in nums:
    print(obj.search(nums, target))



