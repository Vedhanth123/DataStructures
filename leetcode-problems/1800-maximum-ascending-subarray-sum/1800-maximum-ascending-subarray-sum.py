class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        s = 0
        max_sum = 0

        stack = []

        for x in range(len(nums)):
            
            if(stack and stack[-1] < nums[x]):
                stack.append(nums[x])
                s += nums[x]
            
            else:
                stack = [nums[x]]
                s = nums[x]
            
            max_sum = max(max_sum, s)
        
        return max_sum
