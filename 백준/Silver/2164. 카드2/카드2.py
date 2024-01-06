from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
card = deque([])
for i in range(1, n+1):
    card.append(i)

while len(card) != 1:
    card.popleft()
    if len(card) == 1:
        break
    tmp = card.popleft()
    card.append(tmp)

print(*card)