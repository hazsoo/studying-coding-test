def isPrime(x):
    if x < 2:
        return False
    i = 2
    while i*i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

n = int(input())
a = list(map(int, input().split()))
cnt = 0

for x in a:
    if isPrime(x):
        cnt += 1

print(cnt)