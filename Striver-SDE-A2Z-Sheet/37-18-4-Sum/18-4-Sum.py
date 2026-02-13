from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        '''
            Didn't work
        '''
        # Let's try to solve this problem by first sorting the nums array
        # Let's put a pointer at the most left and d pointer at the most right
        # as the numbers are sorted we will check for the array we already tried that right

        '''
            Trying to put 3 sum into this problem 
            (I know the TC would be O(n^3) but this problem's contraints can handle it)
        '''
        nums.sort()
        n = len(nums) - 1
        answers = []
        print(nums)
        def threeSum(a):

            for b in range(a+1, n-1):
                c = b + 1
                d = n

                if(b > 0 and nums[b] == nums[b-1]):
                    continue
                while(c < d):
                    
                    
                    sum_ = nums[b] + nums[c] + nums[d]
                    print(a,b,c,d, sum_)
                    if(sum_ == -nums[a]):
                        answers.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        d -= 1
                        while(c < d and nums[c] == nums[c-1]):
                            c += 1
                        while(c < d and nums[d] == nums[d + 1]):
                            d -= 1

                    elif(sum_ > -target):
                        c += 1
                    else:
                        d -= 1    

        for a in range(n-2):

            # now 3 sum would come in here

            # skipping the numbers
            if(a > 0 and nums[a] == nums[a-1]):
                continue
            
            threeSum(a)
        
        print(answers)
        return answers


Solution().fourSum(nums = [1,0,-1,0,-2,2], target = 0)