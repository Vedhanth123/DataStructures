from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        helper_index = 0

        for x in range(1,len(nums)):

            if(nums[x-1] != nums[x]):
                helper_index += 1
                nums[helper_index] = nums[x]
        
        return helper_index

obj = Solution()
obj.removeDuplicates([1,1,2])