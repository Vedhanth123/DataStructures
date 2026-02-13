from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(numbers) - 1

        while(left < right):

            sum_ = numbers[left] + numbers[right]
            if(sum_ == target):
                return [left, right]
            elif(sum_ < target):
                left += 1
            else:
                right -= 1

obj = Solution()
obj.twoSum(numbers = [2,7,11,15], target = 9)
        