import sys
input = sys.stdin.readline
n = int(input())
a = [0]
for _ in range(n):
    a.append(float(input()))
for i in range(2, n+1):
    a[i] = max(a[i-1] * a[i], a[i])
print('{:.3f}'.format(max(a)))