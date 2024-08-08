def solution(numbers):
    n = len(numbers)
    res = [0]*n
    stack = []
    for i in range(n-1,-1,-1):
        if not stack:
            res[i] = -1
        else:
            while stack:
                if numbers[i] < stack[-1]:
                    res[i] = stack[-1]
                    break
                stack.pop()
                if not stack:
                    res[i] = -1
        stack.append(numbers[i])
    return res