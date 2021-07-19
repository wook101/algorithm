def solution():
    n,m = map(int,input().split())
    trust_tmp = list(map(int,input().split()))
    parties = [ list(map(int,input().split()))[1:] for _ in range(m)]
    party_check = [0]*m
    trust_people = [0]*n
    if trust_tmp[0]==0: return m


    trust_tmp = trust_tmp[1:]

    #진실을 알고 있는 사람 체크
    for tp in trust_tmp:
        trust_people[tp-1]=1

    while trust_tmp:
        tp = trust_tmp.pop()
        for i in range(m):
            if not tp in parties[i]:
                continue
            #진신을 알고있는 사람이 포함된 파티의 모든 사람들을 다시 trust_tmp에 넣고 다시 체크
            for people in parties[i]:
                if not trust_people[people-1]:
                    trust_tmp.append(people)
                    trust_people[people-1]=1
            #해당 파티는 제외시키기
            party_check[i]=1

    return party_check.count(0)


print(solution())