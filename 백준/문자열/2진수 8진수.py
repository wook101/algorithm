#11001100
a = input()
b = [4,2,1]
if len(a)%3==2:
    a="0"+a
elif len(a)%3==1:
    a ="00"+a

result=""
for i in range(0,len(a),3):
    st = a[i:i+3]
    tmp=0
    for j in range(len(st)):
        if st[j]=="1":
            tmp+=b[j]
    result +=str(tmp)
print(result)