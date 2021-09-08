def getParent(parent, node1):
    if parent[node1] == node1:
        return node1
    return getParent(parent, parent[node1])


def union(parent, node1, node2):
    p1 = getParent(parent, node1)
    p2 = getParent(parent, node2)
    if p1 < p2:
        parent[p2] = p1
    else:
        parent[p1] = p2


def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)]

    # 1.최소 비용으로 오름차순 정렬
    costs = sorted(costs, key=lambda x: x[2])
    for cost in costs:
        node1, node2, curCost = cost
        if getParent(parent, node1) != getParent(parent, node2):  # 2사이클이 아니면
            union(parent, node1, node2)                           # 3.두 노드를 union
            answer += curCost

    return answer