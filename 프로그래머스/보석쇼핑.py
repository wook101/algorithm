def solution(gems):
    minSection = float('inf')
    result = []
    data = {}
    gemsCnt = len(set(gems))

    for i in range(len(gems)):
        gem = gems[i]
        if gem in data:
            del data[gem]
        data[gem] = i

        if len(data) == gemsCnt:
            for g in data:
                first = data[g]
                break
            last = i
            curSection = last-first
            if curSection < minSection:
                minSection = curSection
                result = [first+1, last+1]

    return result

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))