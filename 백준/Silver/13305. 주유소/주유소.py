import sys
input = sys.stdin.readline
n = int(input())
km = list(map(int, input().split()))
price = list(map(int, input().split()))
min_price = price[0]
ans = 0
for i in range(n-1):
    if min_price > price[i]:
        min_price = price[i]
    ans += min_price*km[i]
print(ans)