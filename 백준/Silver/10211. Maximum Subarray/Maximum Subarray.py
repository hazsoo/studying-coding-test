import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    dp = [0]*n
    dp[0] = x[0]
    for i in range(1, n):
        dp[i] = max(x[i], dp[i-1] + x[i])
    print(max(dp))