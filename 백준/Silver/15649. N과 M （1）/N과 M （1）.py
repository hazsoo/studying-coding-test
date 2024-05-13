import sys
n, m = map(int, input().split())
use = [False] * (n+1)
res = [0] * m
def go(index, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str, res))+'\n')
        return
    for i in range(1, n+1):
        if use[i]:
            continue
        use[i] = True
        res[index] = i
        go(index+1, n, m)
        use[i] = False

go(0, n, m)