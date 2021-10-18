#나의 풀이
def solution(n, left, right):
    result=[]
    x1,y1 = left//n,left%n
    x2,y2 = right//n,right%n

    while x1!=x2 or y1!=y2:
        result.append(max(x1,y1)+1)
        y1+=1
        if y1==n:
            x1+=1
            y1=0
    result.append(max(x2,y2)+1)

    return result


#참고 풀이
def solution(n, left, right):
    result = []
    for i in range(left,right+1):
        result.append(max(i//n,i%n)+1)
    return result