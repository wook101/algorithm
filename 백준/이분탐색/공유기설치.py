n,c=map(int,input().split())
arr=[int(input()) for _ in range(n)]

arr.sort()
start,end=1,arr[-1]-arr[0] #최소, 최대간격 인덱스
while start<=end:
    mid = (start+end)//2   #현재 간격 크기
    last,cnt=0,1 #마지막 설치한 공유기 위치, 현재까지 설치한 공유기 수
    for idx in range(1,len(arr)):    #공유기 설치 알고리즘
        if arr[idx]-arr[last]>=mid : #현재 간격에 조건에 해당하면 집에 공유기를 설치한다.
            cnt += 1
            last = idx
    if c > cnt:  #C(공유기의 개수)가 (cnt)현재 설치한 공유기수 보다 크면 mid(현재 간격)을 줄인다.
        end=mid-1
    elif c <= cnt: #C(공유기의 개수)가 (cnt)현재 설치한 공유기수 보다 작으면 mid(현재 간격)을 늘린다.
        ans = mid  #설치해야 할 공유기 개수가 일치해도 간격을 늘려 봐야한다.
        start=mid+1
print(ans)


