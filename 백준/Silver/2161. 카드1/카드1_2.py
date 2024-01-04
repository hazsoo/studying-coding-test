import sys
input = sys.stdin.readline
n = int(input())
tmp = []
for i in range(1,n+1):
    tmp.append(i)

ans = []
while 1:
    if len(tmp) == 1:
        print(*ans + tmp)
        break
    ans.append(tmp[0])
    tmp.remove(tmp[0])
    one = tmp[0]
    tmp.remove(one)
    tmp.append(one)
