from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        answer = [1]

        prefix_prod = 1
        for x in range(len(nums)-1):
            prefix_prod *= nums[x]
            answer.append(prefix_prod)
        
        print(answer)

        prefix_prod = 1
        for x in range(len(nums) -1, 0, -1):
            prefix_prod *= nums[x]
            answer[x-1] *= prefix_prod
        
        print(answer)
        

obj = Solution()
obj.productExceptSelf([1,2,3,4])