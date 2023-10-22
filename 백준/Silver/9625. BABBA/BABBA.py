import sys
input = sys.stdin.readline
k = int(input())
dp = [[0]*2 for _ in range(k+1)]
dp[0][0] = 1 # k=0 일 때 a 개수
dp[0][1] = 0 # k=0 일 때 b 개수
dp[1][0] = 0 # k=1 일 때 a 개수
dp[1][1] = 1 # k=1 일 때 b 개수
for i in range(2, k+1):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]
print(dp[k][0], dp[k][1])
