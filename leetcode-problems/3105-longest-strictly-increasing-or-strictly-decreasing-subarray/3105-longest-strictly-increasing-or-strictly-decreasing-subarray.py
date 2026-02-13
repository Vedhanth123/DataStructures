class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        inc_stack = []
        dec_stack = []

        max_inc = 0
        max_dec = 0

        for x in range(len(nums)):

            if(not inc_stack):
                inc_stack.append(nums[x])
            elif(inc_stack[-1] < nums[x]):
                inc_stack.append(nums[x])

            else:
                inc_stack = [nums[x]]
            max_inc = max(max_inc, len(inc_stack))
            
            if(not dec_stack):
                dec_stack.append(nums[x])
            elif(dec_stack[-1] > nums[x]):
                dec_stack.append(nums[x])
            else:
                dec_stack = [nums[x]]
            max_dec = max(max_dec, len(dec_stack))
            
        return max(max_dec, max_inc)