n = int(input())
c = []
for i in range(n):
    c.append(list(map(int, input().split())))
for i in range(1, n):
    c[i][0] = min(c[i-1][1], c[i-1][2]) + c[i][0]
    c[i][1] = min(c[i-1][0], c[i-1][2]) + c[i][1]
    c[i][2] = min(c[i-1][0], c[i-1][1]) + c[i][2]

print(min(c[n-1]))