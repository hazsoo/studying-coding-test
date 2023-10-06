import sys
input = sys.stdin.readline
s1 = list(input().rstrip())
s2 = list(input().rstrip())
dp = [0]*len(s1)
for i in range(len(s2)):
    cnt = 0
    for j in range(len(s1)):
        if cnt < dp[j]:
            cnt = dp[j]
        elif s2[i] == s1[j]:
            dp[j] = cnt + 1
print(max(dp))