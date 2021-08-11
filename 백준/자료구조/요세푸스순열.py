'''
7 3
1234567     []      2
124567      [3]     4
12457       [3,6]
1457        [3,6,2] 1
<3, 6, 2, 7, 5, 1, 4>
'''

def solution():
    n,k = map(int,input().split())
    arr = list(range(1,n+1))
    idx = k-1
    result = []
    while True:                     #O(n*(n+1)//2)  시간복잡도 n이 최대 5000이므로 약 12,500,000번의 연산..
        popNum = arr.pop(idx)       #리스트(arr)에서 현재 인덱스(idx)의 요소를 꺼낸다.
        result.append(str(popNum))  #꺼낸 요소를 임시 리스트(result)에 저장
        if not arr: break
        if idx+k-1 > len(arr)-1:    #인덱스 값이 배열의 길이를 넘어가면
            idx=(idx+k-1)%len(arr)  #나머지 연산으로 꺼낼 인덱스의 위치를 지정해준다.
        else:
            idx+=k-1

    return '<'+', '.join(result)+'>'    #result에 담긴 요소들을 출력!

