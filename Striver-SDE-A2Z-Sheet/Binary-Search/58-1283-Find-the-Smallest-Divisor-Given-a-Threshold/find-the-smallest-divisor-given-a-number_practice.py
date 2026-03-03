from typing import List
import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        left = 1
        right = sum(nums)
        answer = float('inf')
        while(left <= right):

            mid = left + (right - left) // 2

            # find the result
            result = 0
            for num in nums:
                result += math.ceil(num / mid)
                
            if(result <= threshold):
                answer= min(answer, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return answer

        
print(Solution().smallestDivisor(nums = [1,2,5,9], threshold = 6))
