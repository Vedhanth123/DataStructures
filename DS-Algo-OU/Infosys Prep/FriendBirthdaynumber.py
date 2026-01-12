n = 2
k = 2

dp = [0] * (n+1)

for x in range(1, n+1):

    dp[x] = dp[x-1] + 