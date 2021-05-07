def solution():
    mushs = [int(input()) for _ in range(10)]
    total = 0
    for i in range(10):
        total += mushs[i]
        if total == 100:    #합이 100이면 종료
            return 100
        elif total > 100:   #합이 100보다 큰 경우
            if i == 0:      #첫번재 요소가 100보다 크면 첫번째 요소 반환
                return mushs[i]
            else:
                if abs(total - mushs[i] - 100) < abs(total - 100):  #현재까지 합과 이전까지의 합중 100에 더 가까운 합 반환
                    return total - mushs[i]
                else:
                    return total
    return total            #합이 100미만 일때
print(solution())