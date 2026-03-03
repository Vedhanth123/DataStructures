from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)
        answer = float('inf')
        while(left <= right):

            mid = left + (right - left) // 2

            timeTaken = 0
            for bananas in piles:
                timeTaken += math.ceil(bananas / mid)
            
            if(timeTaken <= h):
                right = mid - 1
                answer = min(answer, mid)
            else:
                left = mid + 1
        
        return answer
    
print(Solution().minEatingSpeed(piles = [3,6,7,11], h = 8))