class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        prefix_prod = 1
        suffix_prod = 1

        maxi = float('-inf')


        for x in range(len(nums)):

            if(prefix_prod == 0):
                prefix_prod = 1
            if(suffix_prod == 0):
                suffix_prod = 1
            
            prefix_prod *= nums[x]
            suffix_prod *= nums[-(x+1)]
        
            maxi = max(maxi, max(prefix_prod, suffix_prod))
    
        return maxi
            
            