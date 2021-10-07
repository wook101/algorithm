'''
4 6
a t c i s w
'''

from itertools import combinations

def check(pw):  #모음1개이상, 자음2개이상 체크하기
    vowel_cnt, cons_cnt=0,0
    for i in range(len(pw)):
        if pw[i] in ['a','e','i','o','u']:
            vowel_cnt+=1
        else:
            cons_cnt+=1
    if vowel_cnt>=1 and cons_cnt>=2:
        return True
    return False


def solution():
    L,C=map(int,input().split())
    arr = input().split()
    arr.sort()
    for pw in list(combinations(arr,L)):
        if check(pw): print(''.join(pw))
