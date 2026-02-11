from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        sum_ = 0
        count = 0   
        hashMap = {0:1}

        for x in range(len(nums)):

            sum_ += nums[x]
            target = sum_ - x
            if(target in hashMap):
                count += hashMap[target]
            hashMap[sum_] = hashMap.get(sum_, 1)
        
        return count
