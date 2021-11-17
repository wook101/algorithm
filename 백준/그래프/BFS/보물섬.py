'''
5 7
WLLWWWL
LLLWLLL
LWLWLWW
LWLWLLL
WLLWLWW
'''
from collections import deque
import sys
def bfs(i,j,n,m,matrix):
    visited = [[False] * m for _ in range(n)]
    visited[i][j] = True
    q = deque()
    q.append((i,j,0))
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    max_count = 0
    while q:
        x,y,cost=q.popleft()
        for i in range(4):
            rx = x+dx[i]
            ry = y+dy[i]
            if rx<0 or ry<0 or rx>=n or ry>=m or visited[rx][ry] or matrix[rx][ry]!='L':
                continue
            q.append((rx,ry,cost+1))
            visited[rx][ry]=True

        if not q:
            max_count = cost

    return max_count


def solution():
    n,m = map(int,sys.stdin.readline().split())
    matrix = [list(sys.stdin.readline()) for _ in range(n)]
    res = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j]=='W':continue
            count = bfs(i,j,n,m,matrix)
            if res<count:
                res = count

    return res


print(solution())