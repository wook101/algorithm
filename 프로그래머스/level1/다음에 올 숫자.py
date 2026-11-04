def solution(c):
    a,b = c[1]-c[0], c[2]-c[1]
    return c[-1]+a if a==b else c[-1]*(b//a)