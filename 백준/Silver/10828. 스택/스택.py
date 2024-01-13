from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
d = deque([])

for _ in range(n):
    command = input().split()
    if command[0] == 'push':
        d.append(command[1])
    elif command[0] == 'pop':
        if d:
            print(d.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(d))
    elif command[0] == 'empty':
        if d:
            print(0)
        else:
            print(1)
    elif command[0] == 'top':
        if d:
            print(d[-1])
        else:
            print(-1)