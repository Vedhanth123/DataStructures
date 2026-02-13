class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        answer = float('inf')

        left = 0
        right = len(nums) - 1
        while (left <= right):

            mid = left + (right - left) // 2

            if(nums[left] <= nums[mid]):
                answer = min(answer, nums[left])
                left = mid + 1
            elif(nums[mid] <= nums[right]):
                answer = min(answer, nums[mid])
                right = mid - 1
        return answer