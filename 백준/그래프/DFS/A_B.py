def dfs(startA,startB,startCnt):
    stack = list()
    stack.append([startA,startB,startCnt])
    while stack:
        a,b,cnt = stack.pop()
        if a==b:
            res.append(cnt)
        a1=a*2
        a2=int(str(a)+"1")
        if a1<=b:
            stack.append([a1,b,cnt+1])
        if a2<=b:
            stack.append([a2,b,cnt+1])

A,B=map(int,input().split())
res = []
dfs(A,B,1)
if res:
    print(min(res))
else:
    print(-1)


