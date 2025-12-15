def solution():
    A,B = input().split()
    arr = []
    for i in range(len(B)-len(A)+1):
        cnt=0
        for j in range(len(A)):
            if A[j]!=B[i:i+len(A)][j]:
                cnt+=1
        arr.append(cnt)
    return min(arr)
print(solution())