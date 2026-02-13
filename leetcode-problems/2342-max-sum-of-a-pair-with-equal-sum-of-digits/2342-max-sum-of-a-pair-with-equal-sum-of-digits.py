class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        sum_of_digits = {}
        answer = -1
        for x in range(len(nums)):

            digit_sum = 0
            num = nums[x]
            while(num != 0):
                digit_sum += num % 10
                num //= 10
            
            if(digit_sum in sum_of_digits):
                heapq.heappush(sum_of_digits[digit_sum], -nums[x])
            else:
                sum_of_digits[digit_sum] = [-nums[x]]
        
        for key,val in sum_of_digits.items():

            if(len(val) >= 2):
                answer = max(answer, -heapq.heappop(val) + (-heapq.heappop(val)))
        
        return answer