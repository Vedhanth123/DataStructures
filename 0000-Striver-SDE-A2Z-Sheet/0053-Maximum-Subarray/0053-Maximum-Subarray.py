class Solution:
    def maxSubArray(self, nums: list[int]) -> list:

        # optimal approach:
        # kadane's algorithm:
        # Go from left to right and take the sum_ with you but... if the sum reaches < 0 then reinitialize the sum
        # At each iteration check if this is the maximum sum so far, it then update the sum

        sum_ = 0
        answer = float('-inf')
        answer_corr = [-1,-1]
        left = 0

        for x in range(len(nums)):

            sum_ += nums[x]
            if(sum_ < 0):
                sum_ = 0
                left = x

            if(sum_ > answer):
                answer_corr[0] = left
                answer_corr[1] = x
                answer = max(answer, sum_)

        return nums[answer_corr[0]: answer_corr[1]+1]
