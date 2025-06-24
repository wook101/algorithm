n = int(input())
arr = [ int(input()) for _ in range(n)]
dp = [0]*n

#최소횟수 = 전체길이(n) - LIS(가장 긴 증가하는 수열 길이)
#LIS O(N^2)
for i in range(n):
    dp[i] = 1
    for j in range(i+1):
        if arr[j] < arr[i] and dp[i] < dp[j]+1:
            dp[i]+=1

print(n-max(dp))