n = int(input())
s = [0]
for _ in range(n):
    s.append(int(input()))
d = [0]*(n+1)
if n <= 2:
    print(sum(s))
else:
    d[1] = s[1]
    d[2] = s[1] + s[2]
    for i in range(3, n+1):
        d[i] = max(d[i-3] + s[i-1] + s[i], d[i-2] + s[i])

    print(d[n])