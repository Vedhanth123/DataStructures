class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        majorityElement = 0
        majorityElementCount = 1

        for x in range(len(nums)):

            if(nums[x] != majorityElement):
                majorityElementCount -= 1
            else:
                majorityElementCount += 1

            if(majorityElementCount == 0):
                majorityElement = nums[x]
        
            print(nums[x], majorityElement, majorityElementCount)
        
        return majorityElement
            

print(Solution().majorityElement([8,8,7,7,7]))