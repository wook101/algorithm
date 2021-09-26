def binearySearch(n,cores): #이분탐색의 lower bound: 찾고자 하는 값이 n값 이상인 지점을 end에서 반환
    start,end=1,500000000
    while start<end:
        time = (start+end)//2
        job_amount = sum([time//core for core in cores])
        if n<=job_amount:
            end=time
        else:
            start=time+1
    return end


def solution(n, cores):
    if n<=len(cores): return n
    n-=len(cores)
    cur_time = binearySearch(n,cores)                                         #시간을 기준으로 이분탐색, 현재시간
    n-= sum([(cur_time-1)//core for core in cores])                           #현재 시간 작업량 - 이전 시간까지의 작업량
    temp = [idx+1 for idx in range(len(cores)) if cur_time%cores[idx]==0]     #현재 time에 작업을 수행하는 해당하는 core들을 배열의 위치를(인덱스+1) 넣음
    return temp[n-1]                                                          #(현재 작업량 - 한시간전 작업량)으로 마지막 작업 위치를 구한다.


#print(solution(13+5,[6,2,7,5,3]))
