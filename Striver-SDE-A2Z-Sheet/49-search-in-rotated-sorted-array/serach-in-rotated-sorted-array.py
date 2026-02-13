from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)
        left = 0
        right = n - 1

        def binarysearch(left, right):

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return -1

        while left <= right:
            mid = left + (right - left) // 2

            # check if the left array is sorted
            if nums[left] <= nums[mid] and nums[left] <= target <= nums[mid]:
                return binarysearch(left, mid)
            elif nums[mid] <= nums[right] and nums[mid] <= target <= nums[right]:
                return binarysearch(mid, right)
            elif nums[left] <= nums[mid] and not (nums[left] <= target <= nums[mid]):
                left = mid + 1
            else:
                right = mid - 1

        return -1 if (nums[mid] != target) else mid


print(Solution().search(nums=[4, 5, 6, 7, 8, 1, 2, 3], target=3))
