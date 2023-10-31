import sys
input = sys.stdin.readline
n, k = map(int, input().split())
a = []
for _ in range(n):
    a.append(int(input()))
a2 = a[::-1]
ans = 0
for i in range(len(a2)):
    if a2[i] <= k:
        ans += k // a2[i]
        k = k % a2[i]
print(ans)