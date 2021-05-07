import math
def solution(begin, end):
    answer = []
    for i in range(begin, end + 1):
        for j in range(2, int(math.sqrt(i)) + 1):   #제곱근까지 소수판별
            if i%j==0 and i//j<=10000000:           #블록이 10,000,000까지 있음
                answer.append(i // j)
                break
        else:
            answer.append(1)

    if begin == 1:
        answer[0] = 0

    return answer
print(solution(1,10))