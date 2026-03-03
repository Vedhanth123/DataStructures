class Solution:
    def countGoodNumbers(self, n: int) -> int:

        MOD = 10**9 + 7

        def rec(x, n):
            if n <= 1:
                return x
            if n % 2:
                return x * rec(x, n - 1) % MOD
            else:
                return rec(x * x, n // 2) % MOD

        if n == 1:
            return 5
        elif n % 2 == 0:
            return (rec(5, n // 2) * rec(4, n // 2)) % MOD
        else:
            return (5 * rec(5, (n - 1) // 2) * rec(4, (n - 1) // 2)) % MOD


for x in range(1, 12):
    if x % 2 == 0:
        print(f"{x} = {Solution().countGoodNumbers(x)} * 4")
    else:
        print(f"{x} = {Solution().countGoodNumbers(x)} * 5")

# print(Solution().countGoodNumbers(3))
