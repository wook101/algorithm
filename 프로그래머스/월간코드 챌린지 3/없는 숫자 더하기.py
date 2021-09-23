def solution(numbers):
    return sum({n for n in range(10)}-set(numbers))


#더 깔끔한 코드
def solution(numbers):
    return 45 - sum(numbers)