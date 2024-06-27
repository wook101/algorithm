def solution(plans):
    res = []
    stop = []
    for i in range(len(plans)):
        h, m = plans[i][1].split(':')
        plans[i][1] = int(h) * 60 + int(m)
        plans[i][2] = int(plans[i][2])
    plans = sorted(plans, key=lambda x: x[1])
    for i in plans:
        print(i)
    return res


solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]])