'''
7 8 2
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
-1 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0
'''
import sys
from collections import deque
r,c,t= map(int, sys.stdin.readline().split())
matrix=[list(map(int,sys.stdin.readline().split())) for _ in range(r)]

dx=[0,0,-1,1]
dy=[-1,1,0,0]
cleaner = []
tmp = deque()
for _ in range(t):
    for x in range(r):
        for y in range(c):
            if matrix[x][y]==-1:
                cleaner.append(x)
            elif matrix[x][y]!=0:
                dust = matrix[x][y]//5
                for i in range(4):
                    nx=x+dx[i]
                    ny=y+dy[i]
                    if nx<0 or ny<0 or nx>=r or ny>=c or matrix[nx][ny]==-1 or dust==0:
                        continue
                    tmp.append([x,y,nx,ny,dust])

    while tmp:
        A,B,C,D,E = tmp.popleft()
        matrix[A][B]-=E
        matrix[C][D]+=E

    #공기청정기 가동
    upX,downX=cleaner[0],cleaner[1]

    #상단 회전
    for j in range(upX-1,0,-1):
        matrix[j][0]=matrix[j-1][0]
    for j in range(c-1):
        matrix[0][j] = matrix[0][j+1]
    for j in range(upX):
        matrix[j][c-1] = matrix[j+1][c-1]
    for j in range(c-1,1,-1):
        matrix[upX][j]=matrix[upX][j-1]
    matrix[upX][1]=0

    #하단 회전
    for j in range(downX+1,r-1):
        matrix[j][0]=matrix[j+1][0]
    for j in range(c-1):
        matrix[r-1][j] = matrix[r-1][j+1]
    for j in range(r-1,downX,-1):
        matrix[j][c-1] = matrix[j-1][c-1]
    for j in range(c-1,1,-1):
        matrix[downX][j]=matrix[downX][j-1]
    matrix[downX][1]=0


result = 0
for p in range(r):
    for q in range(c):
        if matrix[p][q]==-1:
            continue
        result+=matrix[p][q]
print(result)
