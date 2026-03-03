from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        sumOfNums = sum(nums)

        left = max(nums)
        right = sumOfNums
        answer = float("-inf")
        while left <= right:
            mid = left + (right - left) // 2

            maxSum = mid
            subarrayCount = 1
            subarraySum = 0
            localAnswer = float('-inf')
            for num in nums:
                if subarraySum + num > maxSum:
                    subarrayCount += 1
                    localAnswer = max(localAnswer, subarraySum)
                    subarraySum = num
                else:
                    subarraySum += num


            subarrayCount += 1
            print(maxSum, subarrayCount)
            if subarrayCount >= k:
                left = mid + 1
                if subarrayCount == k:
                    answer = max(answer, localAnswer)
            else:
                right = mid - 1

        return answer


nums = [2, 3, 1, 2, 4, 3]
k = 5
print(Solution().splitArray(nums, k))
