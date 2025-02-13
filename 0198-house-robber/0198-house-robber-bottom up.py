class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if(len(nums) == 1):
            return nums[0]
        if(len(nums) == 2):
            return max(nums)
        
        mem = [0] + [nums[0],nums[1]] + [-1] * (len(nums)-2) 

        for x in range(2,len(nums)+1):

            mem[x] = max(nums[x-1] + mem[x-2], mem[x-1])
        
        return mem[-1]
        


                