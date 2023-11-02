import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
b = b[::-1]
ans = 0
for i in range(n):
    ans += a[i]*b[i]
print(ans)