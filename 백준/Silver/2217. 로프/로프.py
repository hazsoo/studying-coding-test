import sys
input = sys.stdin.readline
n = int(input())
r = [int(input()) for _ in range(n)]
r.sort()
ans = 0
for i in range(n):
    ans = max(ans, r[i]*(n-i))
print(ans)