from typing import List


class Solution:
    def validStrings(self, n: int) -> List[str]:

        answer = []

        def helper(index, string, length):

            if index >= length - 1:
                answer.append(string)
                return

            if string[-1] == "1":
                helper(index + 1, string + "1", length)
                helper(index + 1, string + "0", length)
            else:
                helper(index + 1, string + "1", length)

        helper(0, "0", n)
        helper(0, "1", n)

        return answer
