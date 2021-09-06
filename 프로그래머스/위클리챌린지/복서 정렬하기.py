def solution(weights, head2head):
    result = []
    player_cnt = len(weights)
    tmp = [[0]*4 for _ in range(player_cnt)]
    for i in range(player_cnt):
        N_cnt = head2head[i].count("N")
        W_cnt = head2head[i].count("W")
        wins = W_cnt/(player_cnt-N_cnt) if N_cnt!=player_cnt else 0
        tmp[i][0]=wins
        for j in range(player_cnt):
            if head2head[i][j]=='W' and weights[i]<weights[j]: tmp[i][1]+=1
        tmp[i][2]=weights[i]
        tmp[i][3]=i+1
    for y in sorted(tmp,key=lambda x : (-x[0],-x[1],-x[2],x[3])): result.append(y[3])
    return result


solution([50,82,75,120],["NLWL","WNLL","LWNW","WWLN"])	#[3,4,1,2]
solution([145,92,86],["NLW","WNL","LWN"])	            #[2,3,1]
solution([60,70,60],["NNN","NNN","NNN"])                #[2,1,3]