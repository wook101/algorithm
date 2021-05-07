from itertools import combinations
from collections import deque
def bfs(graph, case, virus, N, wallCnt, res):
    visit = [[0]*N for _ in range(N)]
    visitCnt = 0
    maxTime = 0
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    q = deque()
    for i in case:
        vX,vY,vTime = virus[i]
        q.append([vX,vY,vTime])
        graph[vX][vY] = vTime
        visit[vX][vY]=1
        visitCnt+=1

    while q:
        x,y,curTime = q.popleft()
        maxTime = max(maxTime,curTime)              #바이러스를 모든곳에 퍼트릴 수 있는 최소시간 체크
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=N or graph[nx][ny]=='-' or visit[nx][ny]:
                continue
            q.append([nx,ny,curTime+1])
            graph[nx][ny]=curTime+1
            visit[nx][ny]=1
            visitCnt+=1

    if visitCnt+wallCnt!=N*N:           #방문한 곳들, 모든벽들의 합이 전체 크기와 같이 않으면, 바이러스를 퍼트릴 수 없는 곳이 있음
        maxTime = -1
    res.append(maxTime)

def solution():
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    virus,time,wallCnt = [],0,0                                     #바이러스들의 좌표들 담을배열, 현재시간, 모든 벽들의 개수
    for i in range(N):
        for j in range(N):
            if graph[i][j]==2:
                virus.append([i,j,time])
            elif graph[i][j]==1:
                graph[i][j] = '-'
                wallCnt+=1

    res = []                                                        #최소 시간들을 담을 리스트
    for case in combinations([i for i in range(len(virus))], M):    #모든 바이러스 출발점들을 결정하기 위한 모든 경우
        bfs(graph, case, virus, N, wallCnt, res)

    res = set(res)
    if -1 in res:
        res.remove(-1)
        if len(res)==0:  #모든 경우들이 담긴 집합에서 -1을 제거했을 때 비어있다면 어떻게 바이러스를 놓아도 퍼뜨릴 수 없음
            return -1
    return min(res)
