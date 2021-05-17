def solution():
    h,w=map(int,input().split())
    arr = list(map(int,input().split()))
    block=[[0]*w for _ in range(h)]
    for i in range(w):
        high = arr[i]
        for j in range(h-1,h-high-1,-1):
            block[j][i] = 1

    water=0
    for i in range(h):
        left, right = 0, w-1        #i층에서 양쪽 끝부터 시작해서 기준을 삼을 left, right 블록(1)의 위치를 찾는다.
        while left<w:
            if block[i][left]==1:
                break
            left+=1
        while right>=0:
            if block[i][right]==1:
                break
            right-=1

        for j in range(left,right+1): #모든 i층의 블록(left)와  블록(right) 사이의 빈공간(0)을 카운트한다.
            if block[i][j]==0:
                water+=1

    return water
