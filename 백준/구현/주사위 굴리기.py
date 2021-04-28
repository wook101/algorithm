'''
4 2 0 0 8
0 2
3 4
5 6
7 8
4 4 4 1 3 3 3 2
'''
def move(dice, cmd):
    if cmd==1:  #동
        a,b,c,d = dice[3],dice[0],dice[5],dice[2]     #위,동,서,바닥 = 서,위,바닥,동
        dice[0]=a
        dice[2]=b
        dice[3]=c
        dice[5]=d
    elif cmd==2: #서
        a, b, c, d = dice[2], dice[5], dice[0], dice[3]  # 위,동,서,바닥 = 동,바닥,위,서
        dice[0]=a
        dice[2]=b
        dice[3]=c
        dice[5]=d
    elif cmd==3: #북
        a, b, c, d = dice[4], dice[0], dice[5], dice[1]  # 위,북,남,바닥 = 남,위,바닥,북
        dice[0]=a
        dice[1]=b
        dice[4]=c
        dice[5]=d
    elif cmd==4: #남
        a, b, c, d = dice[1], dice[5], dice[0], dice[4]  # 위,동,서,바닥 = 북,바닥,위,남
        dice[0]=a
        dice[1]=b
        dice[4]=c
        dice[5]=d



n,m,x,y,k=map(int,input().split())
MAP = [[]*m for _ in range(n)]
for i in range(n):
    MAP[i] = list(map(int,input().split()))
cmds = list(map(int,input().split()))
result = []
arr = [0]*6 #주사위 각면의 값들
dice={} #key - 0,1,2,3,4,5 (상단,북면,동면,서면,남면,바닥면), value - 주사위 면의 값을 찾기위한 인덱스
for i in range(6):
    dice[i] = i

#x,y현재 좌표 n,m 세로,가로
for cmd in cmds:
    dx=[0,0,-1,1]
    dy=[1,-1,0,0]
    rx = x+dx[cmd-1]
    ry = y+dy[cmd-1]

    if rx<0 or rx>=n or ry<0 or ry>=m:
        continue

    move(dice, cmd)                 #주사위 이동
    result.append(arr[dice[0]])     #주사위 상단 부분 추가
    if MAP[rx][ry]==0:              #이동한칸에 값이 0이면: 주사위 바닥면값 > 현재칸으로 갱신
        idx = dice[5]
        MAP[rx][ry] = arr[idx]
    else:                           #이동한칸에 값이 0이 아니면: 현재칸값 > 주사위 바닥면으로 갱신
        val=MAP[rx][ry]
        arr[dice[5]]=val
        MAP[rx][ry]=0
    x,y=rx,ry

#결과값 출력
for val in result:
    print(val)