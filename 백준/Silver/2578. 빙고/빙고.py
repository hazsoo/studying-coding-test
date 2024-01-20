import sys
input = sys.stdin.readline

fe = [list(map(int, input().split())) for _ in range(5)]
call = []
for _ in range(5):
    call += list(map(int, input().split()))

def chkBingo():
    bingo = 0

    # 가로
    for b in fe:
        if b.count(0) == 5:
            bingo += 1
    # 세로
    for i in range(5):
        col = 0
        for j in range(5):
            col += fe[j][i]
        if col == 0:
            bingo += 1
    # 대각선
    d1 = 0
    d2 = 0
    for i in range(5):
        for j in range(5):
            if i == j:
                d1 += fe[i][j]
            if i+j == 4:
                d2 += fe[i][j]
    if d1 == 0:
        bingo += 1
    if d2 == 0:
        bingo += 1
    
    return bingo

cnt = 0
for i in range(25):
    for row in range(5):
        for col in range(5):
            if call[i] == fe[row][col]:
                fe[row][col] = 0
                cnt += 1

    if cnt >= 12: # 빙고가 세 개 이상
        res = chkBingo()
        if res >= 3:
            print(i+1)
            break