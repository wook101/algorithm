import heapq
import sys
def solution():
    n = int(sys.stdin.readline())
    arr = [[] for _ in range(200001)]
    h = []
    res = 0
    for _ in range(n):
        deadLine,ramen = map(int,sys.stdin.readline().split())
        arr[deadLine].append(ramen)

    for i in range(len(arr)-1,0,-1):
        for r in arr[i]:
            heapq.heappush(h,-r)
        if h:
            res+=-heapq.heappop(h)
    return res