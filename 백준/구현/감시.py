import copy
import sys
def backtrack(cctvNumbers,cctvLocations,arr,tmp,res):
    if len(tmp) == len(arr):
        res.append(copy.deepcopy(tmp))
        return

    for direction in range(1,arr[len(tmp)]+1):
        tmp.append([cctvNumbers[len(tmp)],direction,cctvLocations[len(tmp)]])
        backtrack(cctvNumbers,cctvLocations,arr,tmp,res)
        tmp.pop()


def solution():
    N,M = map(int, sys.stdin.readline().split())
    matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]


    cctvLocations, cctvCases, cctvNumbers = [],[],[]
    case = {1:4,2:2,3:4,4:4,5:1}
    for i in range(N):
        for j in range(M):
            if matrix[i][j] in {1,2,3,4,5}:
                cctvNumber = matrix[i][j]
                cctvNumbers.append(cctvNumber)
                cctvLocations.append([i,j])
                cctvCases.append(case[cctvNumber])

    tmp, res = [], []
    backtrack(cctvNumbers, cctvLocations, cctvCases, tmp, res)


    #방향과 cctv번호에 따라서 감시영역을 체크한다.
    #4가지방향 1,2,3,4 / 위,우,아래,좌 이동
    detection = {1:{1:[[-1,0]],          #4가지
                    2:[[0,1]],
                    3:[[1,0]],
                    4:[[0,-1]]},
                2:{1:[[-1,0],[1,0]],    #2가지
                   2:[[0,-1],[0,1]]},
                3:{1:[[-1,0],[0,1]],    #4가지
                   2:[[0,1],[1,0]],
                   3:[[1,0],[0,-1]],
                   4:[[0,-1],[-1,0]]},
                4:{1:[[-1,0],[0,1],[1,0]],          #4가지
                   2:[[0,1],[1,0],[0,-1]],
                   3:[[1,0],[0,-1],[-1,0]],
                   4:[[0,-1],[-1,0],[0,1]]},
                5:{1:[[-1,0],[0,1],[1,0],[0,-1]]}}             #1가지

    minCnt = float('inf')

    for cctvs in res:
        matrixTmp = copy.deepcopy(matrix)
        for cctv in cctvs:
            number,direction,location = cctv
            cmd = detection[number][direction]
            for move in cmd:
                x, y = location
                while True:
                    x,y = x+move[0],y+move[1]
                    if x<0 or y<0 or x>=N or y>=M or matrixTmp[x][y] == 6:
                        break
                    if matrixTmp[x][y]==0:
                        matrixTmp[x][y]=7


        cnt=0
        for i in range(N):
            for j in range(M):
                if matrixTmp[i][j]==0:
                    cnt+=1

        minCnt = min(minCnt,cnt)

    return minCnt

print(solution())