import sys
input = sys.stdin.readline
s = int(input())
i = 0
n = 0
while True:
    if s > i:
        i += 1
        s = s-i
        n += 1
    else:
        print(n)
        break