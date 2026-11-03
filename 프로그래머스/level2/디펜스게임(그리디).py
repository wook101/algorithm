# 30 k=2
# [1,5,2,1,3,1,1,1,1000000,1,1,50,1,1000000,1,1,1]
import heapq
def solution(n, k, enemy):
    cur_round = len(enemy)
    heap = []
    sumEnemy = 0
    for i in range(len(enemy)):
        sumEnemy += enemy[i]
        heapq.heappush(heap, -enemy[i])

        if n < sumEnemy:
            if k > 0:
                k -= 1
                sumEnemy -= -heapq.heappop(heap)
            else:
                cur_round = i
                break

    return cur_round