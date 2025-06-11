def solution():
    N,K = map(int, input().split())
    w = list(map(int, input().split()))
    if N==1:
        return 0

    left, right = 0, N-1
    cnt = 0
    w.sort()
    while left < right:
        if w[left] + w[right] <= K:
            left+=1
            right-=1
            cnt+=1
        else:
            right-=1

    return cnt

print(solution())