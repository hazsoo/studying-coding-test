import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
a2 = a[::-1]
dp1 = [1]*n
dp2 = [1]*n
dp3 = [0]*n
for i in range(n):
    for j in range(i):
        # 증가하는 수열
        if a[i] > a[j]:
            dp1[i] = max(dp1[i] ,dp1[j] + 1)
        # 감소하는 수열
        if a2[i] > a2[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)
# 가운데가 큰 수열
for i in range(n):
    dp3[i] = dp1[i] + dp2[n-i-1] - 1

print(max(dp3))