s = int(input())
n = 0
i = 0

while True:
    if s > i:
        i += 1
        s = s - i
        n += 1
    else:
        print(n)
        break