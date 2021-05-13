A,B=map(int,input().split())
arr=[]
cnt,i,t=1,0,1
while True:
    if i==cnt:
        cnt+=1
        i=0
    arr.append(cnt)
    if t==B or cnt==1001:
        break
    i+=1
    t+=1
print(sum(arr[A-1:B]))