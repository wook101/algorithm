def solution(a, b):
    res = 0
    x = 0  # x: 최대공약수
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            x = i

    # 소인수 구하기
    x = b // x
    tmp = set()
    for i in range(2, x + 1):
        while x % i == 0:
            x = x // i
            tmp.add(i)

    for item in list(tmp):
        if item not in [2, 5]:
            return 2
    return 1