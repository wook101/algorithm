'''
3
1001101 10010
1001001 11001
1000111 1010110
'''

def solution():
    n=int(input())
    result=[]
    for _ in range(n):
        a,b=input().split()
        result.append(bin(int("0b"+a,2)+int("0b"+b,2))[2:])
    for res in result: print(res)

