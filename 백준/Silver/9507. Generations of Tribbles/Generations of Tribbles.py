import sys
input = sys.stdin.readline
koong = [0]*68
t = int(input())
for _ in range(t):
    n = int(input())
    if n < 2:
        print(1)
    elif n == 2:
        print(2)
    elif n == 3:
        print(4)
    else:
        for i in range(n+1):
            koong[0] = 1
            koong[1] = 1
            koong[2] = 2
            koong[3] = 4
            koong[i] = koong[i-1] + koong[i-2] + koong[i-3] + koong[i-4]
        print(koong[n])