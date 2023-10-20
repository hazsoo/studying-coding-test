import sys
input = sys.stdin.readline
n = int(input())
dp = [0]*(n+1)
dp[0] = 0
dp[1] = 1 # 상근
for i in range(2, n+1):
    dp[i] = dp[i-1] + 1

print("SK" if dp[n] % 2 == 1 else "CY")