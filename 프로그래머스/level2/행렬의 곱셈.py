def solution(arr1, arr2):
    answer = [[] * len(arr2) for _ in range(len(arr1))]

    for i in range(len(arr1)):  #3
        for j in range(len(arr2[0])): #2
            tmp = 0
            for k in range(len(arr2)): #2
                tmp += arr1[i][k] * arr2[k][j]
            answer[i].append(tmp)

    return answer


