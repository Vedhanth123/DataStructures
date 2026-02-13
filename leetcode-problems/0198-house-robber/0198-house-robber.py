class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if(len(nums) == 1):
            return nums[0]
        if(len(nums) == 2):
            return max(nums)
        
        h1 = nums[0]
        h2 = max(nums[0], nums[1])


        for x in range(2, len(nums)):
            temp = max(h2, h1 + nums[x])
            h1 = h2
            h2 = temp

        
        return h2