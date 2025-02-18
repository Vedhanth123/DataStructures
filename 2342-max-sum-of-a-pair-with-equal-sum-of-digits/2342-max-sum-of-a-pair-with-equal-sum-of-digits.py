class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        max_sum = -1
        sum_of_digits = {}
        for x in range(len(nums)):

            temp = nums[x]
            digit_sum = 0
            while(temp):
                digit_sum += temp % 10
                temp //= 10
            
            if(digit_sum in sum_of_digits):
                heapq.heappush(sum_of_digits[digit_sum], -nums[x])
            else:
                sum_of_digits[digit_sum] = [-nums[x]]
        
        
        for key, val in sum_of_digits.items():

            if(len(val) >= 2):
                n1 = -heapq.heappop(val)
                n2 = -heapq.heappop(val)
                max_sum = max(max_sum, n1+n2)
        
        return max_sum
                

            
        