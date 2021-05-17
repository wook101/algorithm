from collections import deque
import sys

def solution():
    n=int(sys.stdin.readline())
    k=int(sys.stdin.readline())
    matrix = [[0]*n for _ in range(n)]
    for _ in range(k):
        a,b = map(int, sys.stdin.readline().split())
        matrix[a-1][b-1]=2
    changeCnt=int(sys.stdin.readline())
    cmd,path = deque(),deque()
    for _ in range(changeCnt):
        e,f = sys.stdin.readline().split()
        cmd.append([int(e),f])


    x,y,d,time = 0,0,0,1 #시작좌표, 처음 오른쪽방향, 시간
    dx=[0,-1,1,0]        #동북남서 d(방향) - 0123
    dy=[1,0,0,-1]
    rotate = { 0:{"L":1,"D":2},
               1:{"L":3,"D":0},
               2:{"L":0,"D":3},
               3:{"L":2,"D":1}}

    while True:
        matrix[x][y] = 1
        path.append((x,y))

        #t초뒤 방향 변경
        if cmd and time==cmd[0][0]+1:
            tt, r = cmd.popleft()
            d = rotate[d][r]

        nx,ny = x+dx[d],y+dy[d]
        if nx<0 or ny<0 or nx>=n or ny>=n or matrix[nx][ny]==1: #벽이나 자기 몸에 닿으면 종료
            return time

        if matrix[nx][ny]==0:               #뱀 꼬리 갱신
            tailX,tailY = path.popleft()
            matrix[tailX][tailY] = 0

        x,y=nx,ny
        time+=1
