from typing import List
from collections import defaultdict

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        sum_of_nums = sum(nums)

        if(sum_of_nums  % 2):
            return False

        # we have to reach this sum (this is our m)
        required_sum = sum_of_nums // k

        n = len(nums)

        memo = defaultdict(int)
        def rec(index, curr_sum, considered_elements):
        
            if(curr_sum == required_sum):
                memo[(index,curr_sum)] += 1
                return True

            if(curr_sum > required_sum or index >= len(nums)):
                return False
        
            considered_elements.append(nums[index])
            take = rec(index + 1, curr_sum + nums[index], considered_elements)
            considered_elements.pop()
            not_take = rec(index + 1, curr_sum, considered_elements)

            return take or not_take

        rec(0,0,[])
        print(memo)


print(Solution().canPartitionKSubsets(nums = [4,3,2,3,5,2,1], k = 4))
