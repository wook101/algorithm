'''
2
GCF
ACDEB
------
(100G+10C+F) + (10000A+1000C+100D+10E+B)
가장 큰 계수에 해당당하는 알파벳부터 큰 숫자 부여함
'''

n=int(input())
words=[input() for _ in range(n)]
d = {}
for word in words:
    x=1
    for c in word[::-1]:
        if c in d:
            d[c]+=x
        else:
            d[c]=x
        x*=10

result=0
num=9
for i in sorted(d.items(),key=lambda x:-x[1]):
    result += i[1]*num
    num-=1
print(result)