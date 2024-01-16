import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

k = int(input())
for _ in range(k):
    ans = 0
    i, j, x, y = map(int, input().split())
    for row in range(j-1,y):
        for col in range(i-1,x):
            ans += arr[col][row]
    print(ans)