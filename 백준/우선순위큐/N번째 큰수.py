import heapq
def solution():
    n = int(input())
    h = []
    for i in range(n):
        arr = list(map(int,input().split()))
        for j in range(n):
            num = arr[j]
            heapq.heappush(h,num)
            if len(h)>n:
                heapq.heappop(h)

    result=heapq.heappop(h)
    return result

print(solution())