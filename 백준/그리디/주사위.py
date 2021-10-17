'''
3
1 2 3 4 5 6
'''

def min_dice(arr):
    ret = float('inf')
    for st in arr:
        ret = min(ret, sum([data[c] for c in st]))
    return ret

def solution(n,dice):
    #블록 1개 보이는 면 최솟값
    a = min(dice)
    b = min_dice(['AB', 'AD', 'AC', 'AE', 'BC', 'BD', 'BF', 'CE', 'CF', 'DE', 'DF', 'EF'])
    c = min_dice(['ABC', 'ABD', 'ADE', 'ACE', 'BCF', 'BDF', 'CEF', 'DEF'])
    if n==1: return sum(dice)-max(dice)           #블록하나 체크
    if n==2: return 4*b+4*c                       #최상단 모서리(c) 4개, 최하단모서리(b) 4개씩 체크
                                                  #n이 3이상이면 최상단 모서리4개, 최상단 미드 사이드, 모서리4개의 상하 중단 블록들, 나머지 블록

    total_cnt = 5 * (n ** 2) - (8 * n) + 4        #보이는 블록의 전체 개수
    top_middle_cnt=4*n-8                          #최상단 사이드 중단 부분(2면)
    height_corner_cnt=4*n-4                       #각 모서리 높이 부분(2면)
    top_corner_cnt=4                              #최상단 모서리4개(3면)

    result = b*(top_middle_cnt+height_corner_cnt) + c*top_corner_cnt
    extra_cnt = total_cnt - (top_middle_cnt+height_corner_cnt+top_corner_cnt)

    result+= a*extra_cnt                          #나머지(1면)
    return result


n = int(input())
dice = list(map(int,input().split()))
data = {chr(65 + i): dice[i] for i in range(len(dice))}
print(solution(n,dice))