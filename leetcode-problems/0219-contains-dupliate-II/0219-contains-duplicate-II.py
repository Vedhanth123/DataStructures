from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        freq = {}

        for x in range(len(nums)):
            
            if(nums[x] not in freq):
                freq[nums[x]] = set((x,))
            else:
                freq[nums[x]].add(x)
        
        for key, val in freq.items():

            if(len(val) > 1):
                for x in val:
                    if(abs(k-x) )


obj = Solution()
obj.containsNearbyDuplicate([1,2,3,1,5], k=3)