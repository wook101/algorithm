def recursive(arr, k, cases):
    if len(arr) == k:
        cases.append(arr.copy())
        return

    for s in range(1, 4):
        if arr and s == arr[-1]:
            continue
        arr.append(s)
        recursive(arr, k, cases)
        arr.pop()


def dfs(startNode, pipe, adjList, visited, infectList, link):
    stack = [startNode]
    visited[startNode] = 1
    while stack:
        node = stack.pop()
        for adjNode in adjList[node]:
            if not visited[adjNode] and (node, adjNode) in link[pipe]:
                stack.append(adjNode)
                visited[adjNode] = 1
                infectList.append(adjNode)


def solution(n, infection, edges, k):
    # 모든 경우 체크
    cases = []
    recursive([], k, cases)

    # 인접리스트 생성
    adjList = [[] for _ in range(n + 1)]
    link = {1: set(), 2: set(), 3: set()}
    for e in edges:
        adjList[e[0]].append(e[1])
        adjList[e[1]].append(e[0])
        link[e[2]].add((e[0], e[1]))
        link[e[2]].add((e[1], e[0]))

    # infection 노드 기준
    # 파이프 열고, 바이러스 퍼트리기 dfs탐색
    # 탐색후 감염된 노드 감염 리스트에 삽입
    # 감염리스트네 노드 기준으로 다시 파이프열고, 바이러스 퍼트리기 dfs탐색
    # 감염된 총 노드 수 구하기
    res = 0
    for case in cases:
        cnt = 0
        visited = [0] * (n + 1)
        infectList = [infection]
        for pipe in case:
            for node in infectList:
                dfs(node, pipe, adjList, visited, infectList, link)
        cnt += sum(visited)
        res = max(res, cnt)

    return res

'''
n	infection	edges	k	result
10	1	[[1, 2, 1], [1, 3, 1], [1, 4, 3], [1, 5, 2], [5, 6, 1], [5, 7, 1], [2, 8, 3], [2, 9, 2], [9, 10, 1]]	2	6
7	6	[[1, 2, 3], [1, 4, 3], [4, 5, 1], [5, 6, 1], [3, 6, 2], [3, 7, 2]]	3	7
'''