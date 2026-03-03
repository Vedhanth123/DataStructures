from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # There are 4 cases to solve this problem
        # If all the numbers are positive -> Then multiply everyting right
        # If there are even no. of -ve numbers -> Then also multiply everyting
        # If there are odd numbers then you take the prefix of 1's and suffix of the array and max them out (meaning we don't 1 -ve number so we will be having two arrays prefix of the -ve and suffix of the -ve)
        # If there are zeros then we basically split the array by zeros
        # or we play smart by reinitializing our sum


        # optimal approach by our God striver!
        prefix_prod = 1
        suffix_prod = 1
        answer = float('-inf')

        # trying out the prefix prod first
        for x in range(len(nums)):

            prefix_prod *= nums[x]
            if(prefix_prod == 0):
                prefix_prod = 1
            answer = max(answer, prefix_prod)
        
        for x in range(len(nums)-1,-1,-1):
            suffix_prod *= nums[s]
            if(suffix_prod == 0):
                suffix_prod = 1
            answer = max(answer, suffix_prod)

        return answer

Solution().maxProduct([2, 3, -2, 4])
