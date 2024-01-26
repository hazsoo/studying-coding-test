import sys
input = sys.stdin.readline
dp = [[0]*2 for _ in range(41)]
dp[0] = [1,0]
dp[1] = [0,1]
dp[2] = [1,1]
for i in range(3, 41):
    dp[i] = [dp[i-2][0]+dp[i-1][0], dp[i-2][1]+dp[i-1][1]]

t = int(input())
for _ in range(t):
    n = int(input())
    print(*dp[n])
    
    