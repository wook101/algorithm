import random
def soltion():
    lotto = []
    numbers = [i for i in range(1,46)]  #1~45개 숫자가 담긴 리스트

    random.shuffle(numbers)             #리스트 한번 섞어주고
    for _ in range(6):
        num = numbers.pop()             #뒤에서 부터 숫자 6개 뽑음
        lotto.append(num)

    return lotto

print(soltion()) #[15, 1, 26, 36, 38, 8]

