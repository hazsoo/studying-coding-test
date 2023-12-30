import sys
input = sys.stdin.readline
n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            continue
        if i-1 < 0:
            maze[i][j] = maze[i][j] + maze[i][j-1]
            continue
        if j-1 < 0:
            maze[i][j] = maze[i][j] + maze[i-1][j]
            continue
        maze[i][j] = maze[i][j] + max(maze[i-1][j], maze[i][j-1], maze[i-1][j-1])
print(maze[n-1][m-1])