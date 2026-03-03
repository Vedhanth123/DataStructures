from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # chose it unchose it
        answers = []

        def helper(array, index):

            if index == len(nums):
                answers.append(array.copy())
                return

            helper(array, index + 1)
            array.append(nums[index])
            helper(array, index + 1)
            array.pop()

        helper([], 0)
        return answers


print(Solution().subsets([1, 2, 3]))
