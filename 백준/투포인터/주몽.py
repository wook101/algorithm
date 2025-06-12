def solution():
    N = int(input())
    M = int(input())
    w = list(map(int, input().split()))
    if N==1:
        return 0

    left, right = 0, N-1
    cnt = 0
    w.sort()
    while left < right:
        if w[left] + w[right] < M:
            left+=1
        elif w[left] + w[right] > M:
            right-=1
        else:
            left+=1
            right-=1
            cnt+=1

    return cnt

print(solution())