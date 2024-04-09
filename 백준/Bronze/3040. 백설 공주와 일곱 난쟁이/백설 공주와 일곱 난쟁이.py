num = []
for _ in range(9):
    num.append(int(input()))

MUST = 100
summ = sum(num)
flag = True
for i in range(9):
    for j in range(i+1, 9):
        if summ - num[i] - num[j] == MUST:
            numi, numj = num[i], num[j]
            num.remove(numi)
            num.remove(numj)
            flag = False
            break
    if flag == False:
        break
            
for x in range(7):
    print(num[x])