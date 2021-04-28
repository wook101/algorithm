#dp사용
def solution1(n):
    if n<=1:
        return n
    dp=[0]*n
    dp[0],dp[1]=0,1
    for i in range(2,n):
        dp[i]=dp[i-2]+dp[i-1]
    return dp[i]

#변수만 사용
def solution2(n):
    if n<=1:
        return n
    a,b=0,1
    for i in range(2,n):
        b,a=a+b,b
    return b

#k번째 피보나치 수열
k=int(input())
print(solution1(k+1))
print(solution2(k+1))

