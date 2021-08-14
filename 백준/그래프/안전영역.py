def dfs(matrix,i,j,n,height,visited):
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    stack=[[i,j]]
    visited[i][j]=1
    while stack:
        x,y = stack.pop()
        for i in range(4):
            rx=x+dx[i]
            ry=y+dy[i]
            if rx<0 or ry<0 or rx>=n or ry>=n or visited[rx][ry] or matrix[rx][ry]<=height:
                continue
            stack.append([rx,ry])
            visited[rx][ry]=1

def solution():
    n = int(input())
    matrix = [list(map(int,input().split())) for _ in range(n)]

    maxVal = 0
    for i in range(n):
        for j in range(n):
            maxVal = max(maxVal, matrix[i][j])


    result=0
    for height in range(maxVal+1):
        visited = [[0]*n for _ in range(n)]
        cnt=0
        for i in range(n):
            for j in range(n):
                if not visited[i][j] and matrix[i][j]>height:
                    dfs(matrix,i,j,n,height,visited)
                    cnt+=1
        result = max(result,cnt)

    return result

print(solution())