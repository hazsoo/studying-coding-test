import sys
input = sys.stdin.readline
n = int(input())
t = [0]*(n+1)
t[0] = 1
for i in range(1, n+1):
    if i == 1:
        t[1] = t[0]*t[0]
        continue
    for j in range(1, i+1):
        t[i] += t[j-1] * t[i-j]
print(t[n])