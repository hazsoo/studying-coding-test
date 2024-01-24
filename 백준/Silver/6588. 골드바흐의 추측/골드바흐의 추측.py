import sys
input = sys.stdin.readline

MAX = 1000000
check = [0]*(MAX+1)
prime = []
check[0] = check[1] = True

for i in range(2,MAX+1):
    if not check[i]:
        prime.append(i)
        j = i+i
        while j <= MAX:
            check[j] = True
            j += i

prime = prime[1:]

while True:
    n = int(input())
    if n == 0:
        break
    for p in prime:
        if check[n-p] == False:
            print('{} = {} + {}'.format(n,p,n-p))
            break
    else:
        print("Goldbach's conjecture is wrong.")