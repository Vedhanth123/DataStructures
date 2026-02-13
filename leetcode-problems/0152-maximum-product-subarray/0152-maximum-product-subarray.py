class Solution:
    def maxProduct(self, nums):
        
        current_max = nums[0]
        current_min = nums[0]
        global_max = nums[0]

        for x in range(1,len(nums)):


            curr_max = current_max * nums[x]
            current_max = max(curr_max, nums[x], current_min * nums[x])
            current_min = min(curr_max, nums[x], current_min * nums[x])

            global_max = max(global_max, current_max)
        
        return global_max