n, k = map(int, input().split())
temp = 0

for i in range(1, n+1):
    if n % i == 0:
        temp += 1
        if temp == k:
            print(i)
            break

if temp < k:
    print(0)