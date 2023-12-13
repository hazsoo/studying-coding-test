import sys
input = sys.stdin.readline
n = int(input())
f = [0]*(abs(n)+1)
if n < -1:
    f[0] = 0
    f[1] = 1
    for i in range(2, abs(n)+1):
        f[i] = f[i-1] + f[i-2]
        f[i] = f[i] % 1000000000
    print(1 if n % 2 == 1 else -1)
    print(f[abs(n)])
elif n == -1:
    print(1)
    print(1)
elif n == 0:
    print(0)
    print(0)
elif n == 1:
    print(1)
    print(1)
else:
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
        f[i] = f[i] % 1000000000
    print(1)
    print(f[n])