'''
5 2 1
-----
0 0 1
0 0 2
0 0 3
0 0 4
0 0 5

2 5 10


1*10, 1*5 5*1 ,1*2 2*5,

'''
def solution():
    n,k = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(int(input()))

    print(arr)

solution()