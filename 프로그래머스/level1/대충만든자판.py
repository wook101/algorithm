def solution(keymap, targets):
    res = []
    dic = {}
    for key in keymap:
        for i in range(len(key)):
            if key[i] in dic:
                dic[key[i]] = min(dic[key[i]], i + 1)
            else:
                dic[key[i]] = i + 1

    for target in targets:
        cnt = 0
        for key in target:
            if key not in dic:
                cnt = 0
                break
            cnt += dic[key]

        if cnt == 0:
            res.append(-1)
        else:
            res.append(cnt)

    return res

solution(["ABACD", "BCEFD"], ["ABCD","AABB"])