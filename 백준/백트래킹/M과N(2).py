import copy
def backtrack(N,M,tmp,ret):
    if len(tmp)==M:
        if not sorted(tmp) in ret:
            ret.append(copy.deepcopy(tmp))
        return

    for i in range(1,N+1):
        if i in tmp:
            continue
        tmp.append(i)
        backtrack(N,M,tmp,ret)
        tmp.pop()


def solution():
    N,M = map(int,input().split())
    tmp,ret = [],[]
    backtrack(N,M,tmp,ret)

    for arr in ret:
        print(' '.join(map(str,arr)))

solution()

#종료조건: tmp의 길이가 2인경우
#tmp를 정렬했을때 ret에 존재하는 경우 중복이기 때문에 제외
#ret에 존재하지 않는경우 포함
#과정: tmp에 하나씩 원소를 추가하면서 체크
#재귀함수 종료후 돌아와서 tmp에 마지막 원소 제거 > 다시 원소 추가 반복