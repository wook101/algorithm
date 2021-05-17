import sys
import copy
from itertools import combinations


def dfs(tmp_board,visited,startX,startY,n,m):

    stack=[(startX,startY)]

    dx=[0,0,-1,1]
    dy=[1,-1,0,0]

    while stack:
        x,y = stack.pop()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=n or ny>=m or nx<0 or ny<0 or visited[nx][ny] or tmp_board[nx][ny]!=0:
                continue
            stack.append((nx, ny))
            tmp_board[nx][ny]=2
            visited[nx][ny]=1


def solution():
    n,m=map(int,sys.stdin.readline().split())
    board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    arr = []
    for i in range(n):
        for j in range(m):
            if board[i][j]==0:
                arr.append((i,j))

    maxSafe = 0
    for i in combinations(arr,3): #0인위치에 벽 3개 세우기 조합으로 모든 경우 찾음
        tmp_board = copy.deepcopy(board)
        visited = [[0] * m for _ in range(n)]
        for j in i:
            tmp_board[j[0]][j[1]]=1

        #바이러스 퍼트리기 dfs
        for p in range(n):
            for q in range(m):
                if not visited[p][q] and tmp_board[p][q]==2:
                    dfs(tmp_board,visited,p,q,n,m)
                    visited[p][q]=1

        #안전영역 개수 체크
        safe=0
        for p in range(n):
            for q in range(m):
                if tmp_board[p][q]==0:
                    safe+=1
        maxSafe=max(maxSafe,safe)   #최대 안전영역 크기 저장
    return maxSafe
