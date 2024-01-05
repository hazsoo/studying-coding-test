import sys
input = sys.stdin.readline
n = int(input())
stick = []
for _ in range(n):
    stick.append(int(input()))

cnt = 1
max = stick[-1]
for i in range(n-2, 0-1, -1):
    if stick[i] > max:
        cnt += 1
        max = stick[i]

print(cnt)