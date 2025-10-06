from collections import defaultdict
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        max_heap = []

        for key,val in freq.items():
            heapq.heappush(max_heap, (-val,key))
        
        answer = []

        for x in range(k):
            val = heapq.heappop(max_heap)[1]
            answer.append(val)
        
        return answer
    
if __name__ == "__main__":

    obj = Solution()
    obj.topKFrequent(nums = [1,1,1,2,2,3], k = 2)