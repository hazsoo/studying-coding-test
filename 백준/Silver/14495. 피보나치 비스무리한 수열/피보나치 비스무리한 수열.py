import sys
input = sys.stdin.readline
n = int(input())
dp = [0]*(n+1)
if n == 1 or n == 2 or n == 3:
    print(1)
else:
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-3]
    print(dp[n])