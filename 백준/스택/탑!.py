def solution():
    N = int(input())
    tops = list(map(int, input().split()))
    res = []
    stack = []
    dic = {}
    for i in range(N):
        dic[tops[i]] = i+1

    for top in tops:
        while True:
            if not stack:
                res.append(0)
                stack.append(top)
                break
            if top < stack[-1]:
                res.append(dic[stack[-1]])
                stack.append(top)
                break

            stack.pop()

    return ' '.join(map(str, res))

print(solution())