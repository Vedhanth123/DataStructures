from typing import List
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int | float:
        
        left = min(bloomDay)
        right = max(bloomDay)

        answer = float('inf')

        while(left <= right):

            mid = left + (right - left) // 2

            count = 0
            l = 0
            # now iterate through the array in a sliding window manner to check if the boquets can be made
            for r in range(len(bloomDay)):
                if(bloomDay[r] > mid):
                    l = r + 1
                else:    
                    if(r - l + 1 == k):
                        count += 1
                        l = r + 1
            
            if(count >= m):
                right = mid - 1
                answer = min(answer, mid)
            else:
                left = mid + 1
        
        return answer
    
print(Solution().minDays(bloomDay = [1,10,3,10,2], m = 3, k = 1))
        
                