import re
def dfs(caseArr,cur,tmpSet,res):
    if cur+1==len(caseArr):
        if len(tmpSet)==len(caseArr):
            res.add(' '.join(sorted(list(tmpSet)))) #중복 제거를 위해 정렬 후 문자열로 변환 후 추가
        return
    for user in caseArr[cur+1]:
        if not user in tmpSet:
            tmpSet.add(user)
            dfs(caseArr,cur+1,tmpSet,res)
            tmpSet.remove(user)             #return되면 tmpSet에서 전에 있던 user데이터 삭제

def solution(user_id, banned_id):
    caseArr = [[] for _ in range(len(banned_id))]
    for i in range(len(banned_id)):
        for j in range(len(user_id)):
            pettern = banned_id[i].replace("*","\w")
            if re.match(pettern, user_id[j]) and len(user_id[j])==len(banned_id[i]):
                caseArr[i].append(user_id[j])

    #dfs탐색
    res,tmpSet = set(), set()
    for i in range(len(caseArr[0])):
        tmpSet.add(caseArr[0][i])
        dfs(caseArr,0,tmpSet,res)
        tmpSet.clear()

    return len(res)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]	))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]))