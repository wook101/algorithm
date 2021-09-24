def dfs(n, i, j, visited, matrix, puzzleList, flag):
    puzzle = [[i, j]]
    stack = [[i, j]]
    visited[i][j] = 1
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while stack:
        x, y = stack.pop()
        for idx in range(4):
            rx = x + dx[idx]
            ry = y + dy[idx]
            if rx < 0 or rx >= n or ry < 0 or ry >= n or visited[rx][ry] or matrix[rx][ry]!=flag:
                continue
            stack.append([rx, ry])
            puzzle.append([rx, ry])
            visited[rx][ry] = 1
    puzzleList.append(puzzle)

def init_zero(puzzles):
    for puzzle in puzzles:
        x, y = puzzle[0]
        for i in range(len(puzzle)):
            puzzle[i][0]-=x
            puzzle[i][1]-=y
    for i in range(len(puzzles)): puzzles[i].sort(key=lambda x:(x[0],x[1]))     #좌표(0,0)으로 초기화 후 정렬


def rotate(puzzles,n):
    for puzzle in puzzles:
        for i in range(len(puzzle)):
            x,y=puzzle[i]
            puzzle[i]=[y,n-x-1]
    for i in range(len(puzzles)): puzzles[i].sort(key=lambda x:(x[0],x[1]))     #회전 후 정렬


def solution(game_board, table):
    n = len(game_board)
    emptyPuzzleList = []
    board_visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not board_visited[i][j] and not game_board[i][j]:
                dfs(n, i, j, board_visited, game_board, emptyPuzzleList, 0)  #비어 있는 퍼즐 탐색


    insertPuzzleList = []
    table_visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not table_visited[i][j] and table[i][j]:
                dfs(n, i, j, table_visited, table, insertPuzzleList, 1)     #삽일 할 퍼즐 탐색


    e_puzzle_visited = [0]*len(emptyPuzzleList)  #빈 퍼즐이 채워졌는지 여부
    i_puzzle_visited = [0]*len(insertPuzzleList) #삽입퍼즐 끼웠는지 사용 여부

    init_zero(emptyPuzzleList)   #빈 퍼즐 시작 위치 (0,0)을 기준으로 설정

    count=0                     #퍼즐 매칭하기
    for _ in range(4):          #삽입 퍼즐을 4번 90도 회전하면서 빈퍼즐과 맞는 삽입퍼즐이 있는지 확인
        rotate(insertPuzzleList,n)
        init_zero(insertPuzzleList)
        for i in range(len(insertPuzzleList)):
            for j in range(len(emptyPuzzleList)):
                if not i_puzzle_visited[i] and not e_puzzle_visited[j] and insertPuzzleList[i]==emptyPuzzleList[j]:
                    count+=len(insertPuzzleList[i])
                    e_puzzle_visited[j],i_puzzle_visited[i]=1,1
                    break
    return count

solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],[[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]])
