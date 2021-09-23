def solution(numbers):
    return sum({n for n in range(10)}-set(numbers))