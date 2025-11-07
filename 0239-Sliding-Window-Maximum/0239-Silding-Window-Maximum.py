from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        left = 0
        answer = []
        queue = deque()

        for x in range(len(nums)):

            while(queue and nums[x] > nums[queue[-1]]):
                queue.pop()
            
            queue.append(x)
            if(x >= (k-1)):
                answer.append(nums[queue[0]])
                if(queue[0] <= left):
                    queue.popleft()
                left += 1
        
        return answer


obj = Solution()
obj.maxSlidingWindow(nums = [1,-9,8,-6,6,4,0,5], k = 4)