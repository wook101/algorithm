def solution(arr):
    k, i = max(arr), 1
    while True:
        num = k * i
        cnt = 0
        for j in range(len(arr)):
            if num % arr[j] == 0:
                cnt += 1
        if cnt == len(arr):
            answer = num
            break
        i += 1
    return answer