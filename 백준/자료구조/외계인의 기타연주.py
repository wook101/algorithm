#스택으로 구현
#n개의 줄에대한 리스트와 plat을 담을 우선순위큐 사용하기, 효율성 #O(nlogn)알고리즘 구현해야됨
# N ≤ 500,000, 2 ≤ P ≤ 300,000

import heapq
import sys
def solution():
    n,p = map(int,sys.stdin.readline().split())
    data = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    stack = [[] for _ in range(n)]
    cnt = 0

    for i in range(n):  #500,000   ,O(n)
        line, plat = data[i]
        line-=1
        while True:
            if not stack[line]:
                heapq.heappush(stack[line],-plat)
                cnt+=1
                break

            maxNum = -heapq.heappop(stack[line])  #300,000  ,O(logn)
            if plat==maxNum:
                heapq.heappush(stack[line],-maxNum)
                break
            elif plat<maxNum:
                cnt+=1
            elif plat>maxNum:
                heapq.heappush(stack[line],-maxNum)
                heapq.heappush(stack[line],-plat)
                cnt+=1
                break
    return cnt

print(solution())
