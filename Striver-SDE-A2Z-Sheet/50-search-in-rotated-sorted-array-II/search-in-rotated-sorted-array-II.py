class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)

        left = 0
        right = n-1

        while(left <= right):

            mid = left + (right - left) // 2

            if(target == nums[mid]):
                return True
            elif(nums[left] == nums[mid] and nums[mid] == nums[right]):
                left += 1
                right -= 1
            elif(nums[left] <= nums[mid]):
                if(nums[left] <= target <= nums[mid]):
                    right = mid - 1
                else:
                    left = mid + 1
            elif(nums[mid] <= nums[right]):
                if(nums[mid] <= target <= nums[right]):
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False