def dfs1(i, j, n, color, visited, matrix):
    stack = [(i, j)]
    visited[i][j] = 1
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]
    while stack:
        x, y = stack.pop()
        for i in range(4):
            rx = x + dx[i]
            ry = y + dy[i]
            if rx < 0 or ry < 0 or n <= rx or n <= ry or visited[rx][ry] == 1 or matrix[rx][ry] != color:
                continue
            stack.append((rx, ry))
            visited[rx][ry] = 1


def dfs2(i, j, n, color, visited, matrix):
    stack = [(i, j)]
    visited[i][j] = 1
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]
    while stack:
        x, y = stack.pop()
        for i in range(4):
            rx = x + dx[i]
            ry = y + dy[i]
            if rx < 0 or ry < 0 or n <= rx or n <= ry or visited[rx][ry] == 1:
                continue
            if color == "B":
                if matrix[rx][ry] != "B": continue
            else:
                if matrix[rx][ry] == "B": continue

            stack.append((rx, ry))
            visited[rx][ry] = 1


def solution():
    n = int(input())
    matrix = [list(input()) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    cnt1 = 0
    for i in range(n):
        for j in range(n):
            color = matrix[i][j]
            if visited[i][j]==0:
                dfs1(i, j, n, color, visited, matrix)
                cnt1 += 1


    visited = [[0] * n for _ in range(n)]
    cnt2 = 0
    for i in range(n):
        for j in range(n):
            color = matrix[i][j]
            if visited[i][j]==0:
                dfs2(i, j, n, color, visited, matrix)
                cnt2 += 1

    print(cnt1, cnt2)

solution()