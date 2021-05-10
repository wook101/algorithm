K,N = map(int,input().split())

arr,reulst = [],[]
maxNum = 0
for _ in range(K):
    num = input()
    arr.append(num)
    if maxNum < int(arr[-1]):
        maxNum = int(arr[-1])

for i in range(N-K):
    arr.append(str(maxNum))

for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if int(arr[i]+arr[j]) < int(arr[j]+arr[i]):
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp

print(''.join(arr))



