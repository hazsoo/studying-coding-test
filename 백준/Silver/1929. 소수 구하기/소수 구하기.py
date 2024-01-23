MAX = 1000000
chk = [1] * (MAX + 1)
chk[0] = chk[1] = False

for i in range(2, MAX + 1):
    if chk[i]:
        j = i + i
        while j <= MAX:
            chk[j] = False
            j += i

n1, n2 = map(int, input().split())
for i in range(n1, n2 + 1):
    if chk[i] == True:
        print(i)