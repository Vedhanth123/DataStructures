class Solution:
    def getFloorAndCeil(self, nums, x):

        n = len(nums)

        def ceil() -> int:

            left = 0
            right = n - 1
            answer = n

            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] >= x:
                    right = mid - 1
                    answer = mid
                else:
                    left = mid + 1
            
            return answer
        
        def floor() -> int:
            left = 0
            right = n-1
            answer = -1

            while(left <= right):
                mid = left + (right - left) // 2
                if(nums[mid] <= x):
                    left = mid + 1
                    answer = mid
                else:
                    right = mid - 1
            
            return answer

        print(floor())
        # print(ceil())

Solution().getFloorAndCeil(nums =[3, 4, 5, 7, 8, 10], x= 5)