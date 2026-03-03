from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        answer=  n
        right = n-1
        left = 0

        while(left <= right):
            mid = left + (right - left) // 2

            if(nums[mid] >= target):
                answer = mid 
                right = mid - 1
            else:
                left = mid + 1
        
        return answer

print(Solution().searchInsert(nums = [1,1,3,5,6], target = 1))