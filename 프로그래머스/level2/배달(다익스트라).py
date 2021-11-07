import heapq
def dickstra(start,graph,distance):
    q = [(0,start)] #(현재 까지의 누적된 거리, 현재 정점)
    distance[start]=0
    
    while q:
        dist, node= heapq.heappop(q) #가장 짧은 거리를 먼저 뽑음
        if distance[node] < dist:    #이미 처리된 노드 무시
            continue
            
        #현재 노드와 인접한 다음 노드 거리 확인
        for i in graph[node]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                
    
def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    distance = [int(1e9)]*(N+1)
    start=1
    ret = 0
    for info in road:
        a,b,cost = info
        graph[a].append([b,cost])
        graph[b].append([a,cost])
    
    dickstra(start,graph,distance)
    
    for dist in distance[1:]:
        if dist<=K: ret+=1     
    
    return ret
