from collections import defaultdict
def solution(k, tangerine):
    res, cnt = 0, 0
    data = defaultdict(int)
    for i in tangerine:
        data[i] += 1

    for i in sorted(data.items(),key=lambda x:-x[1]):
        if k<=cnt:
            break
        cnt+=i[0]
        res+=1
    return res


solution(6, [1, 3, 2, 5, 4, 5, 2, 3])

