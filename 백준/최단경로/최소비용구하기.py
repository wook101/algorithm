'''
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5
'''
import heapq
import sys

def dickstra(graph,distance,start,end):
    q = []
    distance[start] = start
    heapq.heappush(q,(0,start))    #거리, 노드

    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

    return distance[end]

def solution():
    V = int(sys.stdin.readline().rstrip())
    E = int(sys.stdin.readline().rstrip())
    graph = [[] for _ in range(V+1)]
    distance = [float('inf') for _ in range(V+1)]

    for _ in range(E):
        a,b,c = map(int,sys.stdin.readline().rstrip().split())
        graph[a].append((b,c))

    start,end = map(int,sys.stdin.readline().rstrip().split())
    return dickstra(graph,distance,start,end)

print(solution())

