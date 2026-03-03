class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        left = 1
        right = sum(weights)

        answer = float('inf')

        while(left <= right):

            mid = left + (right - left) // 2

            capacity = mid
            day = 0
            for weight in weights:
                if(capacity - mid <= 0):
                    day += 1
                    capacity -= weight + mid
                else:
                    capacity -= weight
            
            if(day >= days):
                right = mid - 1
                answer = min(answer, mid)
            else:
                left = mid + 1
        
        return answer if (answer != float('inf')) else -1

            
                

