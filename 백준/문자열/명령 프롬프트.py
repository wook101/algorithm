'''
3
config.sys
config.inf
configures
'''

n=int(input())
arr = [input() for _ in range(n)]

result=""
firstStr = arr[0]
for i in range(len(firstStr)): #9
    flag=True
    for j in range(1,n): #2
        if firstStr[i] != arr[j][i]:
            flag=False
            result += "?"
            break
    if flag:
        result+=firstStr[i]

print(result)