def recursion(N):
    if N==0:
        return 1
    return N * recursion(N-1)

def solution():
    N = int(input())
    return recursion(N)

print(solution())