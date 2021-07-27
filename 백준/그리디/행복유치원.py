#1.arr에서 인접한 두개의 키를 골라서 두개키의 차를 tmp배열에 저장한다.
#2.tmp배열을 정렬한다.
#3.tmp배열의 N-K까지의 합이 최소비용이 된다.
def solution():
    N,K = map(int,input().split())
    arr = list(map(int,input().split()))

    tmp = []
    for i in range(len(arr)-1):
        tmp.append(arr[i+1]-arr[i])

    tmp.sort()

    return sum(tmp[:N-K])
