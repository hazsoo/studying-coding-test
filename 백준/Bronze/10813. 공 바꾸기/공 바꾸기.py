n, m = map(int, input().split())
basket = []
for i in range(n+1):
    basket.append(i)

for _ in range(m):
    i, j = map(int, input().split())
    temp = basket[i]
    basket[i] = basket[j]
    basket[j] = temp

for i in range(n):
    print(basket[i+1], end=' ')