n=int(input())
star=1
for i in range(n-1,-1,-1):
    print(" "*i+"*"*star)
    star +=2