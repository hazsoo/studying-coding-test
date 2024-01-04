import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
ans = []
for i in range(n):
    if num[i] == 0:
        ans.append(i+1)
        continue
    ans.insert(i-num[i], i+1)
print(*ans)