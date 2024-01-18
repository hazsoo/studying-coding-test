import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

m, k = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(m)]

ans = [[0]*k for _ in range(n)]
for row in range(n):
    for col in range(k):
        e = 0
        for i in range(m):
            e += a[row][i]*b[i][col]
        ans[row][col] = e

for x in ans:
    print(*x)