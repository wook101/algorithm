import heapq
def solution(n, works):
    if sum(works)<=n: return 0
    arr,result=[],0

    for work in works:
        heapq.heappush(arr,-work)

    while n>0:
        work=-heapq.heappop(arr)
        work-=1
        heapq.heappush(arr,-work)
        n-=1

    for work in arr:
        result+=work*work

    return result
  
  
  # 우선순위 큐에 모든 데이터를 넣는다.
  # 큐에서 가장 큰수를 꺼내어 1을 뺀후 다시 넣는 행위를 N번 반복한다.
  # 배열내에 요소들의 제곱 누적합을 구한다.
