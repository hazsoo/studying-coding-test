import sys, math
input = sys.stdin.readline
n, k = map(int, input().split())
ans = (math.factorial(n) // (math.factorial(k) * math.factorial(n-k))) % 10007
print(ans)