def solution(s, skip, index):
    res = ''
    data = {chr(97+i):i for i in range(26)}
    skip = {data[c] for c in list(skip)}
    for c in s:
        p = data[c]
        cnt = 0
        while cnt < index:
            p += 1
            if p >= 26:
                p%=26
            if p not in skip:
                cnt += 1
        res+=chr(97+p)
    return res