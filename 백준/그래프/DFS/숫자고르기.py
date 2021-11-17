def dfs(n,start_v,arr):
    stack = [start_v]
    visited =[False]*(n+1)

    while stack:
        cur_v = stack.pop()
        if visited[cur_v] and cur_v==start_v:
            return True

        if not visited[cur_v]:
            stack.append(arr[cur_v])
            visited[cur_v]=True

    return False


def resultPrint(res):
    print(len(res))
    for i in res:
        print(i)


def solution():
    n = int(input())
    arr = [0]*(n+1)
    for i in range(n):
        arr[i+1] = int(input())

    res = []
    for i in range(n):
        if dfs(n,i+1,arr):
            res.append(i+1)

    res.sort()
    resultPrint(res)


solution()