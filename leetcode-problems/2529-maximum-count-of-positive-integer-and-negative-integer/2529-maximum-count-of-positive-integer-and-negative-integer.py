class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
        neg_count = 0
        pos_count = 0

        for x in range(len(nums)):

            if(nums[x] > 0):
                pos_count += 1
            if(nums[x] < 0):
                neg_count += 1
        
        return max(pos_count, neg_count)