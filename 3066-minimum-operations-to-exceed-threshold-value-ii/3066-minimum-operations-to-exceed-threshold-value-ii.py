class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        nums_less_k = 0
        for x in range(len(nums)):
            if(nums[x] < k):
                nums_less_k += 1
        
        heapq.heapify(nums)
        counter = 0
        while(nums_less_k != 0):

            n1 = heapq.heappop(nums)
            if(n1 < k):
                nums_less_k -= 1
            n2 = heapq.heappop(nums)
            if(n2 < k):
                nums_less_k -= 1

            n3 = min(n1,n2) * 2 + max(n1,n2)
            if(n3 < k):
                nums_less_k += 1
            heapq.heappush(nums,n3)
            counter += 1
        
        return counter
        
