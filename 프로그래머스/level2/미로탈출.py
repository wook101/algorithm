from collections import deque
def bfs(fx,fy,w,h,maps,visit,option):
    q = deque()
    q.append([fx,fy])
    visit[fx][fy] = 1
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    while q:
        x,y = q.popleft()
        if maps[x][y] == option: # L:레버 or E:출구 인경우 종료
            return visit[x][y]-1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<h and 0<=ny<w and not maps[nx][ny] == 'X' and not visit[nx][ny]:
                q.append([nx,ny])
                visit[nx][ny] = visit[x][y]+1
    return -1

def solution(maps):
    w, h = len(maps[0]), len(maps)
    maps = [list(i) for i in maps]
    sx,sy,lx,ly=0,0,0,0

    for x in range(h):
        for y in range(w):
            if maps[x][y] == 'S':
                sx,sy = x,y
            if maps[x][y] == 'L':
                lx,ly = x,y

    visit = [[0]*w for _ in range(h)]
    a = bfs(sx,sy,w,h,maps,visit,'L') # 시작 -> 레버
    if a==-1:
        return -1

    visit = [[0]*w for _ in range(h)]
    b = bfs(lx,ly,w,h,maps,visit,'E') # 레버 -> 출구
    if b==-1:
        return -1

    return a+b

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"])) #16
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"])) #-1