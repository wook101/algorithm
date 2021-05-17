n=int(input())
stArr = [input() for _ in range(n)]
d={}

for st in stArr:
    if st in d:
        d[st]+=1
    else:
        d[st]=1

d = sorted(d.items(),key=lambda x:(x[1],x[0]))
print(d[-1][0],d[-1][1])