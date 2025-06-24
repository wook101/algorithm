#가장 길이가 긴 공통되는 부분수열

'''
ACAYKP
CAPCA
'''
str1=input()
str2=input()

d = [[0]*len(str1) for _ in range(len(str2))]
d[0][0] = 1 if str1[0]==str2[0] else 0
for j in range(1,len(str1)):
    if str1[j] == str2[0]:
        d[0][j] = 1
    else:
        d[0][j] = d[0][j-1]
for i in range(1,len(str2)):
    if str2[i] == str1[0]:
        d[i][0] = 1
    else:
        d[i][0] = d[i-1][0]
for i in range(1,len(str2)):
    for j in range(1,len(str1)):
        if str2[i]==str1[j]:
            d[i][j]= d[i-1][j-1]+1
        else:
            d[i][j] = max(d[i][j-1], d[i-1][j])

print(d[len(str2)-1][len(str1)-1])
