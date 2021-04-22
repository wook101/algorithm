from collections import deque
import re

def solution(p, arr):
    flag=True
    for f in p:
        if f=="R": #순서 뒤집기
            flag = not flag
        else:
            if not arr:
                return "error"
            else:
                if flag:
                    arr.popleft()
                else:
                    arr.pop()
    if not flag:
        arr.reverse()
    return "["+','.join(map(str, arr))+"]"

T = int(input())
for _ in range(T):
    a=input()
    b=int(input())
    c=deque(map(int,re.findall('\d+',input())))
    print(solution(a,c))

