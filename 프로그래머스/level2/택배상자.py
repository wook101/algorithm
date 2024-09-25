def solution(order):
    res = 0
    stack = []
    p = 0
    num = 1
    while True:
        if p == len(order) or (stack and stack[-1] > order[p]):
            break

        if order[p] == num:
            num += 1
            p += 1
            res += 1
        elif order[p] > num:
            stack.append(num)
            num += 1
        elif stack:
            if order[p] == stack[-1]:
                p += 1
                res += 1
                stack.pop()

    return res