import sys
def dfs(adj,visit,v,res):
    stack =[v]
    visit[v]=1

    while stack:
        node = stack.pop()
        for nextNode in adj[node]:
            if not visit[nextNode]:
                res[nextNode-2]=node
                stack.append(nextNode)
                visit[nextNode]=1


def solution():
    n=int(sys.stdin.readline())
    adj = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a,b = map(int,sys.stdin.readline().split())
        adj[a].append(b)
        adj[b].append(a)

    visit = [0]*(n+1)
    res = [0]*(n-1)
    dfs(adj,visit,1,res)

    for i in res:
        print(i)

#dfs

