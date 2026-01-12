from typing import List
from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        if(h == len(piles)):
            return max(piles)

        left = 1
        right = max(piles) + 1
        answer = float('inf')

        while(left < right):

            mid = (left + right) // 2
            hours = sum(ceil(pile/mid) for pile in piles)
            
            if(hours <= h):
                answer = min(answer, mid)
                right = mid 
            elif(hours > h):
                left = mid + 1

        return answer