'''

8
sbrus.txt
spc.spc
acm.icpc
korea.icpc
sample.txt
hello.world
sogang.spc
example.txt
'''
import sys
n=int(sys.stdin.readline().strip())
strArr = [sys.stdin.readline().strip() for _ in range(n)]
data = {}
for st in strArr:
    key = st.split('.')[1]
    if key in data:
        data[key]+=1
    else:
        data[key]=1
for i in sorted(data.items(),key=lambda x:x[0]):
    print(i[0],i[1])