from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        i = 0
        j = 0

        minHeap = []
        for x in range(len(nums1)):
            sum_ = nums1[x] + nums2[0]
            heapq.heappush(minHeap,((sum_, x,0)))


        answer = []
        while(True):

            # fetch the pair from the heap
            sum_, x,y = heapq.heappop(minHeap)

            # push that to answer
            answer.append([x,y])

            if(len(answer) == k):
                return answer

            # find the smallest sum neighbour and push that to the heap
            newSum = nums1[x] + nums2[y+1]

            heapq.heappush(minHeap,(newSum, x,y+1))

obj = Solution()
print(obj.kSmallestPairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3))
        
