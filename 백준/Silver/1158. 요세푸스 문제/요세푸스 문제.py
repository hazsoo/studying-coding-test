import sys
input = sys.stdin.readline
n, k = map(int, input().split())

arr = [i for i in range(1,n+1)]
idx = 0
ans = []
while arr:
    idx += k-1
    if idx >= len(arr):
        idx %= len(arr)
    ans.append(str(arr.pop(idx)))

print('<', ', '.join(ans), '>', sep='')