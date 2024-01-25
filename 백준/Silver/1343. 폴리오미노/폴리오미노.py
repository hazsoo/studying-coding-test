import sys
input = sys.stdin.readline

board = input()
num = []
cnt = 0
for b in board:
    if b == 'X':
        cnt += 1
        continue
    if b == '.':
        if cnt > 0:
            num.append(cnt)
        num.append('.')
        cnt = 0
        continue
    num.append(cnt)

ans = ''
for i in range(len(num)):
    if num[i] == '.':
        ans += '.'
        continue
    if num[i] % 4 == 0:
        ans += 'AAAA' * (num[i]//4)
    elif num[i] % 4 == 2:
        ans += 'AAAA' * (num[i]//4)
        ans += 'BB'
    else:
        ans = -1
        break

print(ans)