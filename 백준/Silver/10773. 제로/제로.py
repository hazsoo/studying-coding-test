import sys
input = sys.stdin.readline
k = int(input())
num = []

for _ in range(k):
    i = int(input())
    if i == 0:
        num.pop(-1)
        continue
    num.append(i)

print(sum(num))