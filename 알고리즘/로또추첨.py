import random
def solution():
    lotto = []
    numbers = [i for _ in range(1,46)]  #1~45의 숫자가 담긴 리스트

    random.shuffle(numbers)             #리스트 한번 섞어주고
    for _ in range(6):
        num = numbers.pop()             #뒤에서 부터 숫자 6개 뽑음
        lotto.append(num)

    return sorted(lotto)

#로또 자동 5천원
for i in range(5):
    print(solution())
