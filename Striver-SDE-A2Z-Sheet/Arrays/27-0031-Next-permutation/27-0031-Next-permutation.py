from typing import List
class Solution:

    def reverseArray(self, left: int,nums: List[int]) -> None:

        steps = (left + len(nums))//2
        ctr = -1
        for x in range(left, steps):
            nums[x], nums[ctr] = nums[ctr], nums[x]
            ctr -= 1
    

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Brute force will not work for this solution we. The logical bruteforce solution for this problem would be to just create all the permutations of the nums and then finding the next permutation using the linear search
        # bringing the time complexity of this solution to (N!*N)

        # optimal solution
        # from the problem we can see that to find the next permuation of the number
        # we must ensure that the next number of the array we are generating that number must be slightly greater than the current number not massively greater
        # so... we tend to check from the right hand side of the array (because we focus fron the units place)
        # We will try to keep the left hand side of the array as same as possible (if we change then we will be creating a massive differnce between the original one and the current one.)
        # we don't want to do that. 
        # Now... the logic which the striver has told is to

        # 1) start from the right hand side of the array (leave the units place as you cannot swap with one integer)
        # 2) go from n-2 to the front of the array. 
        # 3) If you find a dip in the array.
        # 4) break the loop and store that index where the dip has occurred
        # 5) Now... again reiterate from the right hand side of the array (this time consider the units place tooo)
        # 6) Find the number which is just greater than the number but.. it must be the smallest one
        # 7) put that newly found number in the index.. But.. store the number from that index in a seperate variable
        # 8) Now... sort the numbers which are right side of the index


        # 1) start from the right hand side of the array (leave the units place as you cannot swap with one integer)
        index = -1
        for x in range(len(nums)-2,-1,-1):

            # 3) If you find a dip in the array.
            # 4) break the loop and store that index where the dip has occurred
            if(nums[x] < nums[x+1]):
                index = x
                break
        
        # special case if the array is in descending order then finding return the sorted array
        if(index == -1):
            nums.sort()
            return

        # 5) Now... again reiterate from the right hand side of the array (this time consider the units place tooo)

        for x in range(len(nums)-1,index-1,-1):
            if(nums[x] > nums[index]):
                nums[index], nums[x] = nums[x], nums[index]
                break
            
        
        self.reverseArray(index+1,nums)
        print(nums)

        
Solution().nextPermutation([4,2,0,2,3,2,0])