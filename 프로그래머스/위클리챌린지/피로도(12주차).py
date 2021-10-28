from itertools import permutations
def solution(k, dungeons):
    n = len(dungeons)
    maxCount=0;
    for case in list(permutations([i for i in range(n)],n)):
        cnt=0
        cur_k=k
        for j in case:
            need, cost=dungeons[j]
            if cur_k>=need:
                cur_k-=cost
                cnt+=1
        maxCount=max(maxCount,cnt)
    return maxCount
  
  
#던전의 길이가 1이상 8이하이다.
#던전의 참여 순서를 바꿔가면서 모든 경우를 구한다. permutataions(순열)을 이용한다.
#순열로 모든 경우를 구했을때 최대 8!=40320개의 경우를 체크하면서 던전에 참여할 수 있는 최대값을 구해주면 된다.
