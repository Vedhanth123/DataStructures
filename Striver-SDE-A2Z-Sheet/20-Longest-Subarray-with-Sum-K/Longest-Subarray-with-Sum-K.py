# example:
'''
Example 1:
Input:
 nums = [10, 5, 2, 7, 1, 9], k = 15  
Output:
 4  
Explanation:
 The longest sub-array with a sum equal to 15 is [5, 2, 7, 1], which has a length of 4. This sub-array starts at index 1 and ends at index 4, and the sum of its elements (5 + 2 + 7 + 1) equals 15. Therefore, the length of this sub-array is 4.

Example 2:
Input:
 nums = [-3, 2, 1], k = 6  
Output:
 0  
Explanation:
 There is no sub-array in the array that sums to 6. Therefore, the output is 0.

'''


class Solution():
    
    def longestSubarraywithSumK(self, array: list[int], k: int)-> int:

        '''
        # default size of the subnarray is 0 (since we haven't found any subarray yet.)
        
        # Algorithm (Brute force):
        # 1) We will try for every subarray starting from the left most.
        # 2) IF we found a subarray of sum k then we will pause the the inner loop and start with left + 1 to find another subarray
        # 3) Also we will update the maxSize variable

        answer = 0
        for left in range(len(array)):

            sum_ = 0
            right = left
            while(right < len(array)):
                sum_ += array[right]
                right += 1
                if(sum_ == k):
                    answer = max(answer, right - left)
                    break
            
        return answer
        '''

        # optimal solution
        answer = 0

        # a classic sliding window problem
        # logic: if the sum of the sliding window exceeds by k then shrink the window
        # If the sum in the sliding window is less than k then increase the sliding window
        # if the sum of the sliding window is k then find the length of the sliding window and compare that to the answer you have

        right = 0
        left = 0
        sum_ = 0
        while(right < len(array)):

            while(left < len(array) and sum_ > k):
                sum_ -= array[left]
                left += 1
                
            if(sum_ == k):
                answer = max(answer, right - left)

            sum_ += array[right]
            right += 1
        
        return answer
            



print(Solution().longestSubarraywithSumK([10, 5, 2, 7, 1, 9],15))


'''
[10, 5, 2, 7, 1, 9]
'''
