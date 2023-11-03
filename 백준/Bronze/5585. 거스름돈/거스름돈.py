import sys
input = sys.stdin.readline
price = int(input())
pay = 1000
change = pay - price
l = [500, 100, 50, 10, 5, 1]
ans = 0
for i in range(len(l)):
    if change == 0:
        break
    if change >= l[i]:
        ans += change // l[i]
        change = change % l[i]
print(ans)