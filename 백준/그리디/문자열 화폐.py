def solution():
    N, X = map(int, input().split())
    res = []
    arr = [0] * N
    value = 26
    if N > X or value*N < X: return "!"

    for i in range(N - 1, -1, -1):
        if value + i <= X:
            arr[i] = 26
            X -= value
        elif X == i:
            arr[i] = 1
            X -= 1
        else:
            arr[i] = X - i
            X = i - 1

    for num in arr:
        res.append(chr(num + 64))

    return ''.join(res)

print(solution())

#뒤에서 부터 Z를 추가해야 X값과 동일하고 사전순으로 가장 제일 앞에 있는 문자열을 알아낼 수 있다.
#Z를 추가 할수 없는 시점에 Z에 제일 가까운 알파벳을 추가한다.
#그 후 나머지 앞부분은 A로 채운다.
