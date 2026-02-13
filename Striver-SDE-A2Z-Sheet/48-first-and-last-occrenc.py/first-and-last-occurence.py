from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)

        # I have to find the first and the last occurence of the elements right
        def getFirstOccurence() -> int:


            left = 0
            right = n-1
            answer = -1

            while(left <= right):

                mid = left + (right - left) // 2
                if(nums[mid] >= target):
                    right = mid - 1
                    answer = mid
                else:
                    left = mid + 1
            
            return answer
        
        def getLastOccurence() -> int:

            left = 0
            right = n-1
            answer = n
            
            while(left <= right):

                mid = left + (right - left) // 2

                if(nums[mid] <= target):
                    left = mid + 1
                    answer = mid
                else:
                    right = mid - 1
            
            return answer

        firstOccurence = getFirstOccurence() 
        lastOccurence = getLastOccurence()

        if(lastOccurence < n and nums[lastOccurence] != target):
            lastOccurence = -1
        if(nums[firstOccurence] != target):
            firstOccurence = -1

        print(firstOccurence, lastOccurence)
        return [firstOccurence, lastOccurence]

Solution().searchRange(nums = [5,7,7,8,8,10], target = 8)
Solution().searchRange(nums = [5,7,7,8,8,10], target = 6)
