def solution(k, score):
    data,res = [],[]
    for i in range(len(score)):
        data.append(score[i])
        data = sorted(data)[::-1][:k]
        res.append(data[-1])
    return res