import sys
n=int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
stack = []
result = [0]*n
for i in range(len(arr)-1,-1,-1):
    num = arr[i]
    if stack:
        while True:
            if not stack:
                stack.append(num)
                result[i]=-1
                break
            if num < stack[-1]:
                result[i]=stack[-1]
                stack.append(num)
                break
            else:
                stack.pop()
    else:
        stack.append(num)
        result[i]=-1

print(' '.join(map(str,result)))