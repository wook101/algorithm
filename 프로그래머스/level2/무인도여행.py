def dfs(startX, startY, w, h, maps, visited):
    res = 0
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    stack = [[startX, startY, int(maps[startX][startY])]]
    visited[startX][startY] = 1
    while stack:
        x, y, day = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and maps[nx][ny] != 'X' and not visited[nx][ny]:
                stack.append([nx, ny, int(maps[nx][ny])])
                visited[nx][ny] = 1
        res += day
    return res


def solution(maps):
    res = []
    w, h = len(maps[0]), len(maps)
    maps = [list(i) for i in maps]
    visited = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if maps[i][j] != 'X' and not visited[i][j]:
                rtn = dfs(i, j, w, h, maps, visited)
                res.append(rtn)
    if not res:
        return [-1]

    return sorted(res)

solution(["X591X","X1X5X","X231X", "1XXX1"])