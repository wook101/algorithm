def solution(x, y, n):
    answer = -1
    DP = [float('inf') for _ in range(y + 1)]
    DP[x] = 0
    for i in range(x, y + 1):
        if i + n <= y:
            DP[i + n] = min(DP[i + n], DP[i] + 1)
        if 2 * i <= y:
            DP[2 * i] = min(DP[2 * i], DP[i] + 1)
        if 3 * i <= y:
            DP[3 * i] = min(DP[3 * i], DP[i] + 1)

    if DP[y] != float('inf'):
        answer = DP[y]

    return answer

print(solution(10,40,5))