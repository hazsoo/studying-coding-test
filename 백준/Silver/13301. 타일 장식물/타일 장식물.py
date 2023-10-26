import sys
input = sys.stdin.readline
n = int(input())
dp = [0]*(n+1)
for i in range(1, n+1):
    if i == 1:
        dp[i] = 1
        continue
    if i == 2:
        dp[i] = 1
        continue
    dp[i] = dp[i-2] + dp[i-1]

print((dp[n]+dp[n-1])*2 + dp[n]*2)