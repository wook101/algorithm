def solution(s):
    res = []
    x = ""
    tmp = ""
    cnt = 0
    for i in range(len(s)):
        if x == "":
            x = s[i]
            tmp = s[i]
            cnt += 1
            continue
        if x == s[i]:
            cnt += 1
        else:
            cnt -= 1
        tmp += s[i]

        if cnt == 0:
            res.append(tmp)
            x = ""
            tmp = ""
    if len(tmp) > 0:
        res.append(tmp)
    d = {}
    d.keys()
    return len(res)