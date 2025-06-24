# 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18
# 1, 0, 1, 2, 0, 2, 3, 2,  0,  4,  3,  4,  3,  4,  5,  4
def solution():
    N = int(input())
    dp = [-1] * (N+1)
    if N >= 3:
        dp[3] = 1
    if N >= 5:
        dp[5] = 1
    for i in range(6, N+1):
        tmp = []
        if dp[i-3] > 0:
            tmp.append(dp[i-3])
        if dp[i-5] > 0:
            tmp.append(dp[i-5])
        if tmp:
            dp[i] = min(tmp) + 1

    return dp[-1]

print(solution())