def solution():
    st = input()
    arr = st.split(".")
    for i in range(len(arr)):
        if arr[i]=='':
            continue
        if len(arr[i])%4==0:
            arr[i]='AAAA'*(len(arr[i])//4)
        elif len(arr[i])%4==2:
            arr[i]='AAAA'*(len(arr[i])//4) + 'BB'
        else:
            return -1
    return '.'.join(arr)
print(solution())