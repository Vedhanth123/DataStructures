from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        # optimal solution from strivers:
        # convert the numbers to set for faster checking if a number exists in the set
        # now iterate the set
        # if a the curr_num -1 in set then ignore
        # else now go on checking till there are numbers+1 in set
        # count the seq
        # update the max variable

        setofnums = set(nums)
        maxLen = 1

        for num in setofnums:

            if(num-1 not in setofnums):
                count = 0
                tocheck = num+1
                while(tocheck in setofnums):
                    count += 1
                    
                maxLen = max(maxLen, count)

        return maxLen
                    

        ...