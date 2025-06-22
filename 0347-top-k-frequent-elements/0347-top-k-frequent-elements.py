class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)

        heap = []

        for key,val in freq.items():

            heapq.heappush(heap, (-val,key))
        
        answer = []

        for x in range(k):

            answer.append(heapq.heappop(heap)[1])
        
        return answer