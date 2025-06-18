class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = 1
        postfix = 1
        result = [1] * len(nums)

        for x in range(len(nums)):

            result[x] = prefix
            prefix *= nums[x]
        
        for x in range(len(nums)-1,-1,-1):

            result[x] *= postfix
            postfix *= nums[x]

        return result