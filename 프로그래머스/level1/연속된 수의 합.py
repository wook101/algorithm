def solution(num, total):
    result = [i for i in range(num)]
    cur_sum = sum(result)
    while cur_sum!=total:
        if cur_sum > total:
            result.insert(0,result[0]-1)
            cur_sum+=result[0]
            cur_sum-=result.pop()
        else:
            result.append(result[-1]+1)
            cur_sum+=result[-1]
            cur_sum-=result.pop(0)

    return result