import sys
input = sys.stdin.readline
n = int(input())
vote = []
for _ in range(n):
    vote.append(int(input()))

if n == 1:
    print(0)
elif max(vote) == min(vote) == vote[0]:
        print(1)
else:
    cnt = 0
    while 1:
        if max(vote) == vote[0] and vote.count(vote[0]) == 1:
            print(cnt)
            break
        vote[vote.index(max(vote),1)] -= 1
        vote[0] += 1
        cnt += 1