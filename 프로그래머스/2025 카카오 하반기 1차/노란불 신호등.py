def solution(signals):
    arr = []
    cnt = 1
    for signal in signals:
        g, y, r = signal
        arr.append([0] * g + [1] * y + [2] * r)
        cnt *= (g + y + r)
    # 최소 공배수 배열 생성
    for i in range(len(arr)):
        arr[i] *= cnt // len(arr[i])

    for i in range(len(arr[0])):  # 35
        val = []
        for j in range(len(arr)):  # 5
            val.append(arr[j][i])
        if val.count(1) == len(arr):
            return i + 1
    return -1

#           signals	             result
solution([[2, 1, 2], [5, 1, 1]]) #13
solution([[2, 3, 2], [3, 1, 3], [2, 1, 1]])	#11
solution([[3, 3, 3], [5, 4, 2], [2, 1, 2]])	#193
solution([[1, 1, 4], [2, 1, 3], [3, 1, 2], [4, 1, 1]]) #-1