def getGrade(avg):
    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    elif avg >= 50:
        grade = "D"
    else:
        grade = "F"
    return grade


def solution(scores):
    result = []
    n = len(scores)
    for i in range(n):
        tmpSum, tmp = 0, []
        for j in range(n):
            tmpSum += scores[j][i]
            tmp.append(scores[j][i])

        cnt = tmp.count(scores[i][i])
        if (min(tmp) == scores[i][i] and cnt == 1) or (max(tmp) == scores[i][i] and cnt == 1):
            avg = (tmpSum - scores[i][i]) / (n - 1)
        else:
            avg = tmpSum / n

        result.append(getGrade(avg))

    return ''.join(result)

