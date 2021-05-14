def solution(left, right):
    ans = 0
    for num in range(left, right + 1):
        tmp = 0
        for i in range(1, num + 1):
            if num % i == 0:
                tmp += 1
        ans = ans + num if tmp % 2 == 0 else ans - num
    return ans