s = input()
res = []
for i in range(len(s)-1):
    for j in range(i+1,len(s)-1):
        res.append(s[:i+1][::-1]+s[i+1:j+1][::-1]+s[j+1:][::-1])
        print(s[:i+1],s[i+1:j+1],s[j+1:])
res.sort()
print(res[0])