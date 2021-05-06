S = input()
zero,one = [],[]
flag, p = S[0],0
for i in range(1,len(S)):
    if flag!=S[i]:
        if flag=="0":
            flag="1"
        else:
            flag="0"
        if flag=="0":
            one.append(S[p:i])
        else:
            zero.append(S[p:i])
        p=i

#마지막 부분 처리
if p<len(S):
    if S[p:][0]=="0":
        zero.append(S[p:])
    else:
        one.append(S[p:])
print(min(len(one),len(zero)))