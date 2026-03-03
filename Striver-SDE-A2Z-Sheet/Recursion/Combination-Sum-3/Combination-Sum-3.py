from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        answers = []

        def helper(array, k, n, sum_, minimum, used):

            if len(array) == k:
                if sum_ == n:
                    answers.append(array.copy())
                return

            for x in range(minimum, 10):
                if x not in used:
                    array.append(x)
                    used.add(x)
                    helper(array, k, n, sum_ + x, minimum=max(minimum, x),used=used)
                    used.remove(x)
                    array.pop()

        helper([], k, n, 0, 1, set())
        return answers


print(Solution().combinationSum3(n=7, k=3))
