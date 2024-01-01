import sys
input = sys.stdin.readline
n = int(input())
box = list(map(int, input().split()))
dp = [0]*(n+1)
for i in range(n):
    dp[i] = 1
    for j in range(i):
        if box[i] > box[j] and dp[j]+1 > dp[i]:
            dp[i] = dp[j]+1
print(max(dp))