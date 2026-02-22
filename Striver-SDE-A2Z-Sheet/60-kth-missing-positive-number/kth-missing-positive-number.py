from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
            
        left = 0
        right = n-1

        while(left <= right):

            mid = left + (right - left) // 2
            missingNos = arr[mid] - (mid + 1)
            if(missingNos < k):
                left = mid + 1
            else:
                right = mid - 1
            
        missingNos = arr[mid] - (mid + 1)
        if(missingNos < k):
            return arr[mid] + (k - missingNos)
        else:
            return arr[mid] - (missingNos - k) - 1
        
            

        
print(Solution().findKthPositive(arr = [2,3,4,7,11], k = 5))