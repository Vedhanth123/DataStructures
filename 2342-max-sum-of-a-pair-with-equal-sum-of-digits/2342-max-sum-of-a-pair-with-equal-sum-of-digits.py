class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        sum_of_digits = defaultdict(list)

        for x in range(len(nums)):

            digit_sum = 0
            temp = nums[x]
            while(temp):
                digit_sum += temp%10
                temp //= 10
            
            if(len(sum_of_digits[digit_sum]) == 2):
                if(min(sum_of_digits[digit_sum]) < nums[x]):
                    sum_of_digits[digit_sum].remove(min(sum_of_digits[digit_sum]))
                    sum_of_digits[digit_sum].append(nums[x])
            else:
                sum_of_digits[digit_sum].append(nums[x])
        
        max_sum = -1

        for key, val in sum_of_digits.items():

            if(len(val) == 2):
                max_sum = max(max_sum, sum(val))
        
        return max_sum
            

        