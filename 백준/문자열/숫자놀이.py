def solution():
    m,n = input().split()
    data = {"1":"one","2":"two","3":"three","4":"four","5":"five"
            ,"6":"six","7":"seven","8":"eight","9":"nine","0":"zero"}
    arr = []
    result=""
    for num in range(min(int(m),int(n)),max(int(m),int(n))+1):
        st=""
        for c in str(num): st+=data[c]
        arr.append((st,num))

    arr = sorted(arr,key=lambda x:x[0])
    for i in range(len(arr)):
        result+=str(arr[i][1])
        if i%10==9: result+="\n"
        else: result+=" "
    return result