from itertools import combinations
def solution(number):
    res = 0
    for i in combinations(number, 3):
        if sum(i) == 0:
            res+=1
    return res


solution([-2, 3, 0, 2, -5])