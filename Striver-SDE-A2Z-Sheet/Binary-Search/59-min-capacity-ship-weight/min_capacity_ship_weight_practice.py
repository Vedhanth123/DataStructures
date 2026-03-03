from typing import List
import math

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        left = 1
        right = sum(weights)

        answer = float('inf')

        while(left <= right):

            mid = left + (right - left) // 2
            
            print(f"--------------------------- ship weight: {mid} -----------------------------------")
            daysToShip = 1
            remWeight = mid
            for weight in weights:  
                print(f"remWeight = {remWeight}, daysToShip = {daysToShip}, weight = {weight}",end=" | ")
                if(remWeight - weight < 0):
                    daysToShip += 1
                    remWeight = mid
                    if(remWeight - weight < 0):
                        daysToShip = float('inf')
                        break
                remWeight -= weight
                print(f"remWeight = {remWeight}, daysToShip = {daysToShip}")
            if(daysToShip <= days):
                right = mid - 1
                answer = min(answer, mid)
            else:
                left = mid + 1
            print(f"--------------------------- ship weight: {mid} -----------------------------------")
    
        return answer

print(Solution().shipWithinDays(weights = [1,2,3,4,5,6,7,8,9,10], days = 10))

