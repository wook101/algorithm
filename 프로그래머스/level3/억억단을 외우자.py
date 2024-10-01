def solution(e, starts):
    count = [0] * (e + 1)
    for i in range(1, e + 1):
        for j in range(i, e + 1, i):
            count[j] += 1

    dp = [0] * (e + 1)
    dp[e] = e
    for i in range(e - 1, 0, -1):
        if count[i] >= count[dp[i + 1]]:
            dp[i] = i
        else:
            dp[i] = dp[i + 1]

    return [dp[s] for s in starts]