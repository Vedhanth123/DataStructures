from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        # I need two pointers
        # two queues

        # p1 pointer will help me in guiding me to fill the new_array
        # p2 pointer will help me in traversing through the nums
        # pos_queue will store the positive elements also it will maintain the relative order
        # neg_queue will store the negative elements also it will maintain the relative order


        new_array = []
        pos_queue = []
        neg_queue = []

        p2 = 0
        for p1 in range(len(nums)):

            # odd index
            if(p1 % 2):
                
                # check if neg_queue is not empty then pop the element from the queue and done
                if(neg_queue):
                    new_array.append(neg_queue.pop(0))
                else:
                    while(p2 < len(nums) and nums[p2] > 0):
                        pos_queue.append(nums[p2])
                        p2 += 1
                    if(p2 < len(nums)):
                        new_array.append(nums[p2])
            else:

                if(pos_queue):
                    new_array.append(pos_queue.pop(0))
                else:
                    while(p2 < len(nums) and nums[p2] < 0):
                        neg_queue.append(nums[p2])
                        p2 += 1
                    if(p2 < len(nums)):
                        new_array.append(nums[p2])
        
        return new_array
