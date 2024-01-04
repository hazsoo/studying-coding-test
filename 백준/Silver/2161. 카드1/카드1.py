import sys
input = sys.stdin.readline
n = int(input())
card = []
for i in range(1,n+1):
    card.append(i)

ans = []
while len(card) != 0:
    ans.append(card.pop(0))
    if len(card) != 0:
        card.append(card.pop(0))

print(*ans)