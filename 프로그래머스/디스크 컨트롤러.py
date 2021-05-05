from collections import deque
import heapq
def solution(jobs):
    waitQue = [] #대기큐
    workQue = [] #작업큐
    for job in jobs:
        waitQue.append(job)
    waitQue = deque(sorted(waitQue,key=lambda x:x[0]))

    answer=0
    t=0
    while waitQue or workQue:
        while waitQue and waitQue[0][0]<=t:
            reqTime, workTime = waitQue.popleft()
            heapq.heappush(workQue,[workTime, reqTime])

        if workQue:
            work = heapq.heappop(workQue)
            t += work[0]
            answer += t - work[1]
        else:
            t +=1

    return answer//len(jobs)

print(solution([[0, 3], [1, 9], [2, 6]]))