import sys
input = sys.stdin.readline
n = int(input())
r = list(map(int, input().split()))
p = list(map(int, input().split()))
ans = p[0]*r[0]
i = 1
while i <= n-2:
    if p[i] <= p[i+1]:
        ans += p[i]*(r[i] + r[i+1])
        i += 2
    elif p[i] > p[i+1]:
        ans += p[i]*r[i]
        i += 1
print(ans)