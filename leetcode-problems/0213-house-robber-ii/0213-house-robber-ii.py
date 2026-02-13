class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if(len(nums) == 1):
            return nums[0]
        if(len(nums) == 2):
            return max(nums)
        
        def helper(arr):
        
            
            if(len(arr) == 1):
                return arr[0]
            elif(len(arr) == 2):
                return max(arr)
            
            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for x in range(2, len(arr)):
                dp[x] = max(arr[x] + dp[x-2], dp[x-1])
        
            return max(dp[-2:])
        
        return max(helper(nums[:-1]), helper(nums[1:]))


