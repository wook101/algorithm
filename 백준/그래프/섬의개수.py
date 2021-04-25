'''
1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0
'''
from collections import deque
def dfs(startX,startY,h,w,matrix,visit):
    dx = [0,0,1,-1,1,-1,1,-1]
    dy = [1,-1,0,0,1,-1,-1,1]
    stack = deque()
    stack.append((startX, startY))

    while stack:
        x,y = stack.pop()
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<h and 0<=ny<w and not visit[nx][ny] and matrix[nx][ny]:
                visit[nx][ny]=1
                stack.append((nx,ny))
                #dfs(nx, ny, h, w, matrix, visit)
                # 재귀를 사용할 경우 파이썬에서 기본 재귀 깊이가 1000으로 제한되어 있어서 런타임 에러발생
                # 스택으로 구현

while True:
    w,h=map(int,input().split())
    if w==0 and h==0:
        break

    matrix = [list(map(int,input().split())) for _ in range(h)]
    visit=[[0]*w for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if not visit[i][j] and matrix[i][j]:
                visit[i][j]=1
                cnt+=1
                dfs(i,j,h,w,matrix,visit)

    print(cnt)
