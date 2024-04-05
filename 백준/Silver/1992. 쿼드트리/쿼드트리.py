n = int(input())
board = [list(map(int, input())) for _ in range(n)]

def dfs(x, y, n):
    chk = board[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if chk != board[i][j]:
                chk = -1
                break

    if chk == -1:
        print("(", end="")

        n //= 2
        dfs(x, y, n)
        dfs(x, y+n, n)
        dfs(x+n, y, n)
        dfs(x+n, y+n, n)

        print(")", end="")
    elif chk == 1:
        print(1, end="")
    else:
        print(0, end="")

dfs(0, 0, n)