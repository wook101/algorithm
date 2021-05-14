import re
def solution(dartResult):
    res = 0
    arr = re.findall('\d+[SDT]#?|[*]', dartResult)
    bonus = ["S","D","T"]
    for i in range(len(arr)):
        for j in range(len(bonus)):
            if bonus[j] in arr[i]:
                arr[i]=arr[i].replace(bonus[j],"**"+str(j+1))
        if "#" in arr[i]:
            arr[i]=arr[i].replace("#","*-1")

    for i in range(len(arr)):
        if arr[i]=="*":
            arr[i-1]*=2
            if i-2>=0:
                if arr[i-2]=="*":
                    arr[i-3]*=2
                else:
                    arr[i-2]*=2
        else:
            arr[i] =  eval(arr[i])

    for i in range(len(arr)):
        if arr[i]=="*": continue
        res+=arr[i]

    return res
