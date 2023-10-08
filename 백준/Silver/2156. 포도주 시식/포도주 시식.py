import sys
input = sys.stdin.readline
n = int(input())
w = [0]
for _ in range(n):
    w.append(int(input()))
dp = [0]*(n+1)
for i in range(1, n+1):
    if i == 1:
        dp[i] = w[i]
    elif i == 2:
        dp[i] = dp[i-1] + w[i]
    else:
        dp[i] = max(dp[i-3] + w[i-1] + w[i], # 현재 와인 O, 직전 와인 O
                    dp[i-2] + w[i],          # 현재 와인 O, 직전 와인 X
                    dp[i-1])                 # 현재 와인 X
print(dp[n])
