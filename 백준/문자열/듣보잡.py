'''
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton
'''

def solution():
    data={}
    n,m = map(int,input().split())
    for _ in range(n):
        st = input()
        data[st]=1

    for _ in range(m):
        st = input()
        if st in data:
            data[st]+=1
        else:
            data[st]=1
    result=[]
    for i in sorted(data.items(),key=lambda x:x[0]):
        if i[1]>1:
            result.append(i[0])
    print(len(result))
    for i in result:
        print(i)

solution()