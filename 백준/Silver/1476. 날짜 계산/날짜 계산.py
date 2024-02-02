e, m, s = map(int, input().split())
e -= 1
m -= 1
s -= 1
year = 0
while True:
    if year % 15 == e and year % 28 == m and year % 19 == s:
        print(year + 1)
        break
    year += 1