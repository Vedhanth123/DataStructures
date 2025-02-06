class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        
        freq = defaultdict(list)
        answer = 0

        for x in range(len(nums)):

            for y in range(x+1, len(nums)):

                freq[nums[x] * nums[y]].append([nums[x],nums[y]])
        

        for key,val in freq.items():

            if(len(val) > 1):
                answer += 8
        
        return answer

            