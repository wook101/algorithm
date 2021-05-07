n,a,b = map(int,input().split())
roundNum = 0
while a!=b:
    a = a//2+a%2
    b = b//2+b%2
    roundNum+=1
print(roundNum)