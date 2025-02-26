class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
    
        min_prefix_sum = float('inf')
        max_prefix_sum = float('-inf')

        prefix_sum = 0

        for x in range(len(nums)):
            prefix_sum += nums[x]

            min_prefix_sum = min(min_prefix_sum, prefix_sum)
            max_prefix_sum = max(max_prefix_sum, prefix_sum)
        
        return max_prefix_sum - min_prefix_sum