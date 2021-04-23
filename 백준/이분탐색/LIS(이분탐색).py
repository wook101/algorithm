
'''
6
10 20 10 30 20 50

이분탐색을 이용하면 시간복잡도 o(nlogn)
8
10 20 10 30 15 16 17 18
'''


n=int(input())
arr=list(map(int, input().split()))
result = [] #이분탐색으로 생성된 배열

for i in range(n):
    if i==0:
        result.append(arr[0])
        continue
    if arr[i] > result[-1]: #result배열 맨뒤에 삽입
        result.append(arr[i])
    else: #이분탐색 시작 o(logn)
        start,end=0,len(result)-1
        target = arr[i]
        while start<end:
            mid=(start+end)//2
            if result[mid]<target:
                start = mid+1
            elif result[mid]>target:
                end = mid
            else:
                start=end=mid
        result[end] = target
print(len(result))


