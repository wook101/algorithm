'''
5 4
2
8
10
7
'''
def solution():
    egg,m=map(int,input().split())
    pays = [int(input()) for _ in range(m)]
    pays.sort(reverse=True)
    temp = []
    for i in range(len(pays)):
        if egg > 0:
            temp.append((pays[i],pays[i]*(i+1)))
            egg-=1
    temp.sort(key=lambda x: -x[1])
    print(temp[0][0],temp[0][1])

