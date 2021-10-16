def gcd(n,m):
    while n%m!=0:
        mod=m
        m=n%m
        n=mod
    return m

n,m=map(int,input().split(':'))
g=gcd(n,m)
print('%d:%d'%(n//g,m//g))