n = 1000-int(input())
coin = [500,100,50,10,5,1]
cnt,i=0,0
while True:
    if n==0:
        break
    if n>=coin[i]:
        cnt+= n//coin[i]
        n%=coin[i]
    else:
        i+=1
print(cnt)


