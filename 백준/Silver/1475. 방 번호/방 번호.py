import sys
input = sys.stdin.readline
n = int(input())
nlist = list(map(int,str(n)))
set = [0]*10

for i in range(len(nlist)):
    if nlist[i] == 6 or nlist[i] == 9:
        if set[6] < set[9]:
            set[6] += 1
        else:
            set[9] += 1
    else:
        set[nlist[i]] += 1

print(max(set))