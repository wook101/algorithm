import copy
def perm(n,tmp,ret):
    #termination
    if len(tmp)==n:
        ret.append(copy.deepcopy(tmp))
        return
    #process
    for num in range(1,n+1):
        if num in tmp:
            continue
        #recursive
        tmp.append(num)
        perm(n,tmp,ret)
        tmp.pop()


def solution(n):
    ret = []
    perm(n,[],ret)
    return ret

solution(8)