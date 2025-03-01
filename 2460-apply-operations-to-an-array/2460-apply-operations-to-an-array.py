class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for x in range(len(nums)-1):

            if(nums[x] == nums[x+1]):
                nums[x] += nums[x]
                nums[x+1] = 0
        
        insertion_ptr = 0
        for x in range(len(nums)):

            if(nums[x] != 0):
                nums[insertion_ptr] = nums[x]
                insertion_ptr += 1
        
        for x in range(insertion_ptr, len(nums)):
            nums[x] = 0
        
        return nums