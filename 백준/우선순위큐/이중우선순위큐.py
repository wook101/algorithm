#삭제연산시 시간초과, 딕셔너리 생성하여 숫자 카운트 후 체크
import sys
import heapq
T = int(sys.stdin.readline())
for _ in range(T):
    Q = int(sys.stdin.readline())
    minheap, maxheap = [], []
    dicCnt = dict()                                     #key-숫자 : value- 숫자의 개수
    for _ in range(Q):
        cmd,num = sys.stdin.readline().split()
        num=int(num)
        if cmd=='I':
            heapq.heappush(minheap,num)
            heapq.heappush(maxheap,-num)
            dicCnt[num] = dicCnt[num]+1 if num in dicCnt else 1
        else:
            if not minheap or not maxheap:
                continue
            if num==1:
                while maxheap:
                    maxN = -heapq.heappop(maxheap)
                    if dicCnt[maxN]==0:
                        continue
                    dicCnt[maxN]-=1
                    break
            else:
                while minheap:
                    minN = heapq.heappop(minheap)
                    if dicCnt[minN]==0:
                        continue
                    dicCnt[minN]-=1
                    break

    result = []
    while maxheap:
        x=-heapq.heappop(maxheap)
        if dicCnt[x]!=0:
            result.append(str(x))
            break

    while minheap:
        y=heapq.heappop(minheap)
        if dicCnt[y]!=0:
            result.append(str(y))
            break

    if result:
        print(' '.join(result))
    else:
        print("EMPTY")



