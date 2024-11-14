def solution(ingredient):
    res = 0
    stack = []
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == [1,2,3,1]:
            for _ in range(4):
                stack.pop()
            res+=1
    return res