n=int(input())
arr = [[input(),0] for _ in range(n)]

for i in arr:
    tmp=0
    for c in i[0]:
       if c.isdigit():
           tmp+=int(c)
    i[1]=tmp

arr.sort(key=lambda x:(len(x[0]),x[1],x[0]))
for i in arr:
    print(i[0])
