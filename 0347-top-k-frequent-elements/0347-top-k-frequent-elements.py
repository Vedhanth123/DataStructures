class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        freq = defaultdict(int)

        for x in range(len(nums)):

            freq[nums[x]] += 1
        
        for key,val in freq.items():

            heapq.heappush(heap,(-val,key))
        

        result = []

        for x in range(k):
            val,key = heapq.heappop(heap)
            result.append(key)

        return result

