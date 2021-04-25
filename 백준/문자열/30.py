#끝자리가 0
#각자리수의 합이 3의 배수
N=input()

if not '0' in N:
    print(-1)
else:
    sotedN = sorted(N, reverse=True)
    a = sum(map(int,list(sotedN)))
    if a%3==0:
        print(''.join(sotedN))
    else:
        print(-1)