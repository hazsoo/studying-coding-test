import sys
input = sys.stdin.readline

arr = [[0]*100 for _ in range(100)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for row in range(x1,x2):
        for col in range(y1,y2):
            arr[row][col] = 1

ans = 0
for x in arr:
    ans += sum(x)

print(ans)