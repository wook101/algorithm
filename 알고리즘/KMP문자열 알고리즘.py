#접두사,접미사 비교
def piTable(s,pi):
    i = 0
    for j in range(1, len(s)):
        while i > 0 and s[i] != s[j]:
            i = pi[i - 1]
        if s[i] == s[j]:
            pi[j] = i + 1
            i += 1

def KMP(pi,searchStr,targetStr):
    i=0
    for j in range(len(targetStr)):
        while i>0 and searchStr[i]!=targetStr[j]:
            i=pi[i-1]
        if searchStr[i]==targetStr[j]:
            if i==len(searchStr)-1:
                return 1
            else:
                i+=1
    return 0

def solution():
    targetStr=input()
    searchStr=input()

    #접두사,접미사 비교
    pi=[0]*len(searchStr)
    piTable(searchStr,pi)

    #KMP
    return KMP(pi, searchStr, targetStr)

print(solution())



