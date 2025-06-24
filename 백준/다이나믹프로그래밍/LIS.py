n = int(input())
arr = list(map(int,input().split()))
dp= [0]*n
#dp[i] = 1 ~ i-1 번째 원소중 arr[i]번째 보다 작은 수들중 가장큰 db[i-1]+1
dp[0]=1
for i in range(1,n):
    maxVal=0
    for j in range(i):
        if arr[i]>arr[j]:
            maxVal = max(dp[j], maxVal)
    dp[i]=maxVal+1
print(max(dp))