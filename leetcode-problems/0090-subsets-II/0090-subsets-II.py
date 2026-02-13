from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        answer = []

        def helper(nums, temp, index):

            if(index == len(nums)):
                answer.append(temp.copy())
                return
            
            temp.append(nums[index])
            helper(nums, temp, index+1)
            temp.pop()
            while(index < (len(nums)-1) and nums[index] == nums[index+1]):
                index += 1
            
            helper(nums, temp, index+1)
        
        helper(nums, [], 0)
        print(answer)
        
if __name__ == '__main__':
    Solution().subsetsWithDup([1,1,2,2])