def solution():
    arr = []
    while True:
        st = input()
        if set(st) == {'-'}:
            break
        arr.append(st)

    for i in range(len(arr)):
        s = arr[i]
        stack = []
        for c in s:
            if stack and c=="}" and stack[-1]=='{':
                stack.pop()
            else:
                stack.append(c)
        cnt = 0
        for j in range(0,len(stack),2):
            if stack[j]==stack[j+1]:
                cnt+=1
            else:
                cnt+=2
        print(str(i+1)+". "+str(cnt))

solution()