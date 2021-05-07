'''
4
1 10
3 15
1 3
4 8
--------
5
3 15
3 15
3 5
1 15
2 10

결과
10
10
0
15
5
'''
import sys
n=int(sys.stdin.readline())
data=[]
ball = [0]*200001
for i in range(n):
    c,s =map(int,sys.stdin.readline().split())
    data.append([i,c,s])
data.sort(key=lambda x:(x[2],x[1]))

result = []
totalSize,j=0,0
for i in range(len(data)):
    curIdx,color,curSize = data[i]
    while data[j][2] < curSize:
        totalSize += data[j][2]         #총 크기 누적
        ball[data[j][1]] += data[j][2]  #공의색에 대한 공 크기누적
        j+=1
    catchSize = totalSize-ball[color]   #공을 잡은 총 크기 = (공의 현재까지 누적된 크기의합 - 현재 공색에 대한 누적된 크기의합)
    result.append([curIdx,catchSize])

result.sort(key=lambda x:x[0])
for res in result:
    print(res[1])