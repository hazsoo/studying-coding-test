import sys
input = sys.stdin.readline
n = int(input())
word = []
for _ in range(n):
    word.append(input().rstrip())

breaker = False
for i in range(n):
    for j in range(n):
        rword = (''.join(reversed(word[i]))).strip()
        if rword == word[j]:
            lth = len(word[i])
            print(lth, word[i][lth//2])
            breaker = True
            break
    if breaker == True:
        break