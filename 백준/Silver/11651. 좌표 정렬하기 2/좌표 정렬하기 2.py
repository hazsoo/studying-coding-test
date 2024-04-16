n = int(input())
dots = []

for i in range(n):
    x, y = map(int, input().split())
    dots.append([y,x])

dots = sorted(dots)

for y, x in dots:
    print(x, y)