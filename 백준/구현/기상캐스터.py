'''
6 8
.c......
........
.ccc..c.
....c...
..c.cc..
....c...
'''
from collections import deque
H,W = map(int, input().split())
sky = [ deque(input()) for _ in range(H)]
res = [[-1]*W for _ in range(H)]


for i in range(H):
    for j in range(W):
        if sky[i][j] == 'c':
            res[i][j] = 0

minute=1
for _ in range(W-1): #7
    for i in range(H):
        sky[i].appendleft('.')
        sky[i].pop()

    for i in range(H):
        for j in range(W):
            if sky[i][j] == 'c' and res[i][j]==-1:
                res[i][j] = minute
    minute += 1


for arr in res:
    print(' '.join(map(str,arr)))