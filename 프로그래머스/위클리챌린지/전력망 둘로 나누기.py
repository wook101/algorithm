from collections import defaultdict


def getParent(parents, node):
    if parents[node] == node:
        return node
    return getParent(parents, parents[node])


def union(parents, node1, node2):
    p1 = getParent(parents, node1)
    p2 = getParent(parents, node2)
    if p1 < p2:
        parents[p2] = node1
    else:
        parents[p1] = node2


def solution(n, wires):
    result = float('inf')
    for i in range(n - 1):
        parents = [i for i in range(n + 1)]
        data = defaultdict(int)
        for j in range(len(wires)):
            if i == j: continue
            v1, v2 = wires[j]
            union(parents, v1, v2)

        for node in parents[1:]:
            data[getParent(parents, node)] += 1

        diff = abs(list(data.items())[0][1] - list(data.items())[1][1])
        result = min(result, diff)

    return result