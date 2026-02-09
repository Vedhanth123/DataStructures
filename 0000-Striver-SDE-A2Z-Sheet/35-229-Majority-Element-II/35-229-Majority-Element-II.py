from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        # This problem is absolutely same as its predeccessor but with a tiny change
        # the frequency of the elements must be greater than or equal to n//3

        # 1) Brute force approach would be to count each and every element 
        # its time complexity would be O(n^2) and O(1)

        # 2) Hashing solution would be O(1) for time and O(n) for space

        # 3) Moore's Voting Algorithm: according to the Striver
        # instead of considering only 1 number we consider 2 numbers in this case

        el1 = el2 = None
        ctr1 = ctr2 = 0

        for x in range(len(nums)):

            if(ctr1 == 0 and nums[x] != el2):
                ctr1 = 1
                el1 = nums[x]
            elif(ctr2 == 0 and nums[x] != el1):
                ctr2 = 1
                el2 = nums[x]
            elif(nums[x] == el1):
                ctr1 += 1
            elif(nums[x] == el2):
                ctr2 += 1
            else:
                ctr1 -= 1
                ctr2 -= 1
                
        nctr1 = 0
        nctr2 = 0
        for x in range(len(nums)):
            if(nums[x] == el1):
                nctr1 += 1
            elif(nums[x] == el2):
                nctr2 += 1
            
        answers = []

        if(nctr1 > len(nums) // 3):
            answers.append(el1)
        if(nctr2 > len(nums) // 3):
            answers.append(el2)
        
        return answers

        ...
Solution().majorityElement([3,2,3])