n = int(input())
n_nums = sorted(list(map(int, input().split())))
m = int(input())
m_nums = list(map(int, input().split()))

cnt = {}
for i in n_nums:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in m_nums:
    if i in cnt:
        print(cnt[i], end=' ')
    else:
        print(0, end=' ')