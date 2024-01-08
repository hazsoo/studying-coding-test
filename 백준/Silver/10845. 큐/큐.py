import sys, queue
input = sys.stdin.readline

q = queue.Queue()
n = int(input())

for _ in range(n):
    command = input().split()
    if command[0] == 'push':
        q.put(command[1])
    elif command[0] == 'pop':
        if q.empty():
            print(-1)
        else:
            print(q.get())
    elif command[0] == 'size':
        print(q.qsize())
    elif command[0] == 'empty':
        if q.empty():
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if q.empty():
            print(-1)
        else:
            print(q.queue[0])
    elif command[0] == 'back':
        if q.empty():
            print(-1)
        else:
            print(q.queue[-1])