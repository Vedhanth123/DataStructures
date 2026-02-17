class Solution:
    def mySqrt(self, x: int) -> int:

        left = 0
        right = 2**16

        answer = float("-inf")

        while left < right:
            mid = left + (right - left) // 2
            if mid*mid <= x:
                left = mid + 1
                answer = max(answer, mid)
            else:
                right = mid - 1

        return answer


print(Solution().mySqrt(x=36))
