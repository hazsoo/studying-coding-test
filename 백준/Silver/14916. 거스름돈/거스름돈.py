import sys
input = sys.stdin.readline
n = int(input())
dp = [-1]*(n+1)
if n == 1:
    dp[1] = -1
elif n == 2:
    dp[2] = 1
elif n == 3:
    dp[3] = -1
elif n == 4:
    dp[4] = 2
elif n == 5:
    dp[5] = 1
elif n == 6:
    dp[6] = 3
elif n == 7:
    dp[7] = 2
elif n == 8:
    dp[8] = 4
else:
    dp[4] = 2
    dp[5] = 1
    dp[6] = 3
    dp[7] = 2
    dp[8] = 4
    for i in range(9, n+1):
        dp[i] = min(dp[i-2]+1, dp[i-5]+1)
print(dp[n])