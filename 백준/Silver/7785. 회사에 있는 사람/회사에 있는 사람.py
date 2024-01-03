import sys
input = sys.stdin.readline
n = int(input())
tmp = dict()

for _ in range(n):
    name, log = map(str, input().split())
    if log == "enter":
        tmp[name] = log
    else:
        del tmp[name]
        
tmp = sorted(tmp.keys(), reverse=True)
for i in tmp:
    print(i)