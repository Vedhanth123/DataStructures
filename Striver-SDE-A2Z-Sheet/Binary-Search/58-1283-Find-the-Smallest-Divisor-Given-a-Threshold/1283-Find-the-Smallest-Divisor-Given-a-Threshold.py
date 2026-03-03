class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        left = 1
        right = max(nums)

        while(left <= right):

            mid = left + (right - left) // 2

            sum_ = 0
            for num in nums:
                sum_ += math.ceil(num / mid)
            
            if(sum_ <= threshold):
                right = mid - 1
            else:
                left = mid + 1
        
        return left