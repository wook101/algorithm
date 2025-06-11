'''
arr [1, 2, 3, 4, 2, 5, 3, 1, 1, 2]
left 0, right 1 시작
1. sum이 m보다 크면 sum에서 arr[left] 빼주고, left 1증가
2. sum이 m보다 작으면 sum에서 arr[right] 더해주고, right 1증가, right랑 N값이 같은경우 반복문 종료
3. sum이 m과 같으면 sum에서 arr[left] 빼주고, left 1증가, cnt 1증가
'''
def solution():
    N,M = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt = 0
    left, right = 0, 1
    numSum = arr[0]
    while True:
        if numSum > M:
            numSum -= arr[left]
            left += 1
        elif numSum < M:
            if right==N:
                break
            numSum += arr[right]
            right += 1
        else:
            numSum -= arr[left]
            left += 1
            cnt += 1

    return cnt

print(solution())