'''
10101111
01111101
11001110
00000010
2
3 -1
1 1
'''
#      2       6    인덱스
#12시  3시     9시    시계
#1 0   1 0 1 1 1 1  톱니바퀴

# 1-2 / 3시, 9시 / 다른지 같은지 판단하고 회전
# 2-3 / 3시, 9시
# 3-4 / 3시, 9시

# 1234기어의 회전 여부 기록,
# [(1,1),(1,-1),(1,1),(0,-1)] // rotateCheck변수

from collections import deque
def rotateGear(gear,start_gear,direction):
    rotateCheck = [[0,0] for _ in range(4)]
    rotateCheck[start_gear] = [1, direction]

    curGear = start_gear
    for leftGear in range(start_gear-1,-1,-1):
        if gear[leftGear][2] == gear[curGear][6]:
            break
        direction = direction * -1
        rotateCheck[leftGear] = [1,direction]
        curGear = leftGear

    curGear = start_gear
    direction = rotateCheck[start_gear][1]
    for rightGear in range(start_gear+1,4):
        if gear[curGear][2] == gear[rightGear][6]:
            break
        direction = direction * -1
        rotateCheck[rightGear] = [1, direction]
        curGear = rightGear


    for i in range(4):
        check, d = rotateCheck[i]
        if check==1:
            if d==1:
                gear[i].appendleft(gear[i].pop())
            else:
                gear[i].append(gear[i].popleft())


def solution():
    gear = [ deque(list(input())) for _ in range(4)]
    k = int(input())
    cmd = [ list(map(int,input().split())) for _ in range(k)]


    for i in range(k):
        start_gear, direction = cmd[i]
        rotateGear(gear,start_gear-1,direction)


    res = 0
    for i in range(4):
        if gear[i][0]=="1":
            res += 2**i


    return res

print(solution())