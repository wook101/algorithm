'''
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
'''
import sys
import heapq

def get_smallest_node1(distance,visited):
    min_value = float('inf')
    node = 0
    for i in range(1,len(distance)):
        if distance[i]<min_value and not visited[i]:
            min_value = distance[i]
            node = i
    return node


def dickstra1(graph,distance,visited,start): #dickstra1(graph,distance,visited,K) #O(V^2) 시간초과
    distance[start] = 0         #start노드 까지 거리는 0
    visited[start] = True       #start노드 방문
    for i in graph[start]:      #start노드에 연결된 node들 거리 갱신
        distance[i[0]] = i[1]

    for _ in range(len(graph)-1):   #O(V^2) 20000*20000 = 2억
        now = get_smallest_node1(distance,visited) #O(V)  #현재 위치에서 방문 안한 노드중 가장 거리가 짧은 노드 선택
        visited[now] = True                               #노드 방문 처리
        for j in graph[now]:                              #현재 노드와 연결된 다른 노드를 확인하기, 현재 노드까지 거리+다음 노드까지의 거리가 < 다음노드에 정의 되어있는 거리값이면 갱신한다.
            cost = distance[now]+j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

    #출력
    for i in range(1,len(distance)):
        if distance[i]==float('inf'):
            print("INF")
        else:
            print(distance[i])



def dickstra2(graph,distance,start):
    q = []
    distance[start]=0
    heapq.heappush(q,(0,start)) #(거리, 노드)
    while q:
        dist,now = heapq.heappop(q) #O(logE)
        if distance[now] < dist:    #이미 처리가 된 경우이기 때문에 무시한다. 이전 단계에서 넣은 dist값이 현재 now(노드)까지 거리보다 큰 경우 무시한다.
            continue
        #현재 노드에서 인접한 노드에 대해서 최단경로 갱신
        for i in graph[now]:   #O(E)
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

    #출력
    for i in range(1,len(distance)):
        if distance[i]==float('inf'):
            print("INF")
        else:
            print(distance[i])


def solution():
    V,E = map(int, sys.stdin.readline().rstrip().split())
    K = int(sys.stdin.readline().rstrip())

    graph = [[] for _ in range(V+1)]
    distance = [float('inf')]*(V+1)
    for i in range(E):
        u,v,w = map(int,sys.stdin.readline().rstrip().split())
        graph[u].append((v, w)) #노드, 거리

    dickstra2(graph,distance,K) # O(ElogE) > O(ElogV^2) > O(2ElogV) >  O(ElogV) 시간을 줄이기 위해 우선순위큐를 적용한다.

solution()