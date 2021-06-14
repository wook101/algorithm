def solution():
    N,L = map(int,input().split())
    flows = list(map(int,input().split()))
    flows.sort()

    tapeCnt = 1
    position = flows[0]+L-0.5
    for i in range(1,len(flows)):
        if flows[i] < position:
            continue
        position = flows[i]+L-0.5
        tapeCnt += 1

    return tapeCnt

print(solution())
