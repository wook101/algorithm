def solution(board):
    res = 0
    n = len(board)
    tmp = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                tmp[i][j]=1
                if i-1>=0:
                    tmp[i-1][j]=1
                if i+1<n:
                    tmp[i+1][j]=1
                if j-1>=0:
                    tmp[i][j-1]=1
                if j+1<n:
                    tmp[i][j+1]=1
                if i-1>=0 and j-1>=0:
                    tmp[i-1][j-1]=1
                if i-1>=0 and j+1<n:
                    tmp[i-1][j+1]=1
                if i+1<n and j+1<n:
                    tmp[i+1][j+1]=1
                if i+1<n and j-1>=0:
                    tmp[i+1][j-1]=1

    for i in range(n):
        for j in range(n):
            if tmp[i][j] == 0:
                res+=1

    return res