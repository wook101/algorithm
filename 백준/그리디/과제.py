'''
7
4 60
4 40
1 20
2 50
3 30
4 10
6 5
'''
def solution():
    n = int(input())
    project = [list(map(int,input().split())) for _ in range(n)]
    maxDay = max(project)[0]
    project.sort(key=lambda x: (x[1],x[0]),reverse=True)
    score = [0]*maxDay

    for i in range(len(project)):
        d,w = project[i]
        d-=1
        if score[d]==0:
            score[d] = w
        else:
            while 0<=d-1:
                d-=1
                if score[d]==0:
                    score[d]=w
                    break
    return sum(score)
solution()
#1.점수가 높은 순 내림차순 정렬한다, 점수가 같다면 과제 마감일이 낮은순으로 정렬한다.
#2.마감일에 가깝게 점수를 저장해야 한다.
#3.해당 마감일을 인덱스로 가지는 (score[d]) score배열에 점수를 저장한다.
#4.만약 해당 score[d]에 이미 점수가 저장됬으면 마감일을 score[d]기준으로 인덱스를 줄이면서(d-1) 들어갈 공간을 찾는다.
#5.점수가 저장 되어있는 score배열의 합을 반환한다.