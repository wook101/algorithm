def solution(table, languages, preference):
    size = len(table)
    data = [{} for _ in range(size)]
    tmp = [[] for _ in range(size)]
    for i in range(size):
        languList = table[i].split()
        score = size
        tmp[i].append(languList[0])
        for langu in languList[1:]:
            data[i][langu] = score
            score -= 1

    for i in range(size):
        totalScore = 0
        for j in range(len(languages)):
            key = languages[j]
            if not key in data[i]: continue
            preferScore = preference[j]
            languagesScore = data[i][key]
            totalScore += preferScore * languagesScore
        tmp[i].append(totalScore)

    result = sorted(tmp, key=lambda x: (-x[1], x[0]))

    return result[0][0]



a = ["tt","ee"]
print(a.index("ee"))