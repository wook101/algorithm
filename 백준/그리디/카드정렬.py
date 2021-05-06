import sys
import heapq
n = int(sys.stdin.readline())
h = []
for _ in range(n):
    num = int(sys.stdin.readline())
    heapq.heappush(h,num)

res = 0
while len(h)>1:
    a=heapq.heappop(h)
    b=heapq.heappop(h)
    heapq.heappush(h,a+b)
    res+=a+b
print(res)