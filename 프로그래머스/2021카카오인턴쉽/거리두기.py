def isValid(place):
    n=5
    dx = [-1,1,0,0,-2,2,0,0,1,-1,-1,1]
    dy = [0,0,-1,1,0,0,-2,2,1,-1,1,-1]
    for x in range(n):
        for y in range(n):
            if place[x][y] == 'P':
                for i in range(12):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if place[nx][ny] == 'P':
                        flag = abs(abs(dx[i]) - abs(dy[i]))
                        if flag == 0:   # 대각선
                            nx1, ny1 = x + dx[i], y
                            nx2, ny2 = x, y + dy[i]
                            if place[nx1][ny2] == "O" or place[nx2][ny2] == "O":
                                return False
                        elif flag == 1:  # 상하좌우
                            return False
                        elif flag == 2:  # 상하좌우+1
                            nx = x + dx[i - 4]
                            ny = y + dy[i - 4]
                            if place[nx][ny] != "X":
                                return False
    return True

def solution(places):
    result = []
    for place in places:
        if isValid(place):
            result.append(1)
        else:
            result.append(0)
    return result