def solution():
    target = input()
    n = int(input())
    rings = [input() for _ in range(n)]

    count=0
    for ring in rings:
        t=0
        while t < 10:
            tmpStr = ""
            s,i = t,0
            while i < len(target):
                if s==10: s=0
                tmpStr+=ring[s]
                s+=1
                i+=1
            if target==tmpStr:
                count +=1
                break
            t+=1

    return count