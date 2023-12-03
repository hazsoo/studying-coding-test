import sys
input = sys.stdin.readline
r, c, w = map(int, input().split())
rows = r + w - 1
dp = [[0]*(rows) for _ in range(rows)]
for i in range(rows):
    dp[i][0] = 1
    dp[i][i] = 1
for i in range(2, rows):
    for j in range(1, i):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
sum = 0
for i in range(w):
    for j in range(i+1):
        sum += dp[i+r-1][c+j-1]
print(sum)