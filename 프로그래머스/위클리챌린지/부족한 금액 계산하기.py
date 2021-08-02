#count횟수 만큼 price에 곱해서 전체 금액구함
#전체 지불금액(total)이 현재 보유금액(money) 보다 많으면 차를 구한다.
#그렇지 않은경우 0을 리턴

def solution(price, money, count):  #O(N)
    total = 0
    for i in range(1,count+1):
        total += price*i
    result = total-money if total > money else 0
    return result

def solution2(price, money, count): #O(1)
    total = price * count*(count+1) // 2
    result = total-money if total > money else 0
    return result


