import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
dp = [0]*(n+1)
for i in range(n):
    dp[i] = a[i]
    for j in range(i):
        if a[i] > a[j] and dp[j]+a[i] > dp[i]:
            dp[i] = dp[j]+a[i]
print(max(dp))