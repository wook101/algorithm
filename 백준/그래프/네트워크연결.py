#네트워크를 모두연결 하는데 필요한 최소비용 구하기 (크루스칼 알고리즘)
#1.연결 선들의 비용이 작은순으로 정렬한다.
#2.연결 처리여부 - 두 노드의 최종부모가 같지 않다면(싸이클이 발생하지 않는다면) union한다. 부모가 같은 경우 연결되어 있다고 판단 할 수있음

import sys
def getParent(parents,node):
    if parents[node] == node:
        return node
    return getParent(parents, parents[node])

def union(parents,node1,node2):
    parent1 = getParent(parents, node1)
    parent2 = getParent(parents, node2)
    if parent1 < parent2:
        parents[parent2] = parent1
    else:
        parents[parent1] = parent2


def solution():
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    arr = [list(map(int,sys.stdin.readline().split())) for _ in range(m)]

    result = 0
    parents = [ i for i in range(n)]
    for i in sorted(arr,key=lambda x:x[2]):
        a,b,cost = i
        a=a-1
        b=b-1
        if getParent(parents,a)!=getParent(parents,b):
            union(parents,a,b)
            result+=cost

    return result

print(solution())

