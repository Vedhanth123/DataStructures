from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        answers = []

        for x in range(len(nums)-2):

            p1 = x+1
            p2 = len(nums)-1
            toMake = nums[x]

            if(x > 0 and nums[x] == nums[x-1]):
                continue

            while(p1 < p2):
                if(nums[p1] + nums[p2] + nums[x] == 0):
                    answers.append([nums[x], nums[p1], nums[p2]])
                    p1 += 1
                    p2 -= 1
                    while(p1 < p2 and nums[p1] == nums[p1-1]):
                        p1 += 1
                    while(p1 < p2 and nums[p2] == nums[p2+1]):
                        p2 -= 1
                elif(nums[p1] + nums[p2] + toMake > 0):
                    p2 -= 1
                else:
                    p1 += 1

        return answers

Solution().threeSum([-100,-70,-60,110,120,130,160])

