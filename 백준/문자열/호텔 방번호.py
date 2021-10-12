'''
87 104
989 1022
22 25
1234 1234
'''
def solution():
    n,m=map(int,input().split())
    count=0
    for i in range(n,m+1):
        str_i=str(i)
        if len(str_i)==len(set(str_i)): count+=1
    return count

print(solution())