'''
1 0 3
4 2 5
7 8 6
'''
#193425786 > 123456789
from collections import deque
def bfs(s):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()
    q.append(s)
    dist = dict()
    dist[s]=0

    while q:
        now_num = q.popleft()
        if now_num==123456789:
            return dist[now_num]

        now_num = str(now_num)
        idx = now_num.find("9")
        x,y = idx//3, idx%3
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>2 or ny<0 or ny>2:
                continue
            #스왑
            next_num = list(now_num)
            next_num[x*3+y],next_num[nx*3+ny] = next_num[nx*3+ny],next_num[x*3+y]
            next_num=int(''.join(next_num))

            if not dist.get(next_num):
                dist[next_num] = dist[int(now_num)]+1
                q.append(next_num)
    return -1
start = ""
for i in range(3):
    start+=''.join(input().split())
start=start.replace("0","9")
print(bfs(int(start)))