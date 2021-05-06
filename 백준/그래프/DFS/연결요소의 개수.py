#재귀로 하면 런타임에러
def dfs(x):
    for nextX in adj[x]:
        if not visit[nextX]:
            visit[nextX]=1
            dfs(nextX)
#스택으로 구현
def dfs2(x):
    stack=[x]
    visit[x]=1
    while stack:
        curX = stack.pop()
        for nextX in adj[curX]:
            if not visit[nextX]:
                stack.append(nextX)
                visit[nextX]=1

import sys
n,m = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)

visit = [0]*n
cnt = 0
for i in range(n):
    if not visit[i]:
        dfs2(i)
        cnt+=1
print(cnt)