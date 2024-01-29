import sys
input = sys.stdin.readline

n = 9
h = [int(input()) for _ in range(n)]
h.sort()
sumh = sum(h)

for i in range(n):
    for j in range(i+1,n):
        if sumh - h[i] - h[j] == 100:
            for k in range(0,n):
                if i == k or j == k:
                    continue
                print(h[k])
            sys.exit()