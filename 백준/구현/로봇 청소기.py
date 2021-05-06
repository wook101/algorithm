n,m=map(int,input().split())
x,y,d = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
#d = 0북,1동,2남,3서

while True:
    #현재위치 청소
    if matrix[x][y]==0:
        matrix[x][y]=2

    #현재 방향에 따른 왼쪽방향 판별
    #d 0북,1동,2남,3서 부터
    dx=[0,-1,0,1]
    dy=[-1,0,1,0]
    dd=[3,0,1,2]

    #4개의 방향 체크
    check = True
    for i in range(4):
        rx = x+dx[i]
        ry = y+dy[i]
        if 0<=rx<n and 0<=ry<m and not matrix[rx][ry]:
            check = False

    if check:
        # 뒤쪽방향 체크
        bx = [1, 0, -1, 0]
        by = [0, -1, 0, 1]
        rx = x + bx[d]
        ry = y + by[d]
        if 0<=rx<n and 0<=ry<m:
            if matrix[rx][ry]==1: #뒤에 벽이 있어서 후진을 못할 경우 종료
                break
            else: #후진
                x,y =rx,ry
                continue

    #왼쪽 방향 체크
    rx = x+dx[d]
    ry = y+dy[d]
    rd = dd[d]
    d=rd
    if 0<=rx<n and 0<=ry<m and not matrix[rx][ry]: #한칸이동
        x,y=rx,ry

cnt = 0
for i in matrix:
    cnt +=i.count(2)

print(cnt)