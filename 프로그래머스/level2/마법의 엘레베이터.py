def 마법의엘리베이터(s):
    res = 0
    p = 0
    s = str(s)
    for i in range(len(s) - 1, -1, -1):
        num = int(s[i]) + p
        if i == 0:
            if num == 10:
                res += 1
            elif num > 5:
                res += 10-num+1
            else:
                res += num
        else:
            if num == 10:
                p = 1
            elif num < 5:
                res += num
                p = 0
            elif num > 5:
                res += 10 - num
                p = 1
            elif num == 5:
                if int(s[i-1])+1 > 5:
                    p=1
                else:
                    p=0
                res += 5
    return str(res)

#테스트 케이스
print("[6] result: " + 마법의엘리베이터(16))
print("[16] result: " + 마법의엘리베이터(2554))
print("[14] result: " + 마법의엘리베이터(545))
print("[14] result: " + 마법의엘리베이터(555))
print("[11] result: " + 마법의엘리베이터(485))
print("[11] result: " + 마법의엘리베이터(155))
print("[10] result: " + 마법의엘리베이터(154))
print("[9] result: " + 마법의엘리베이터(45))
print("[2] result: " + 마법의엘리베이터(999))
print("[2] result: " + 마법의엘리베이터(99))
print("[6] result: " + 마법의엘리베이터(95))
print("[2] result: " + 마법의엘리베이터(9))
print("[8] result: " + 마법의엘리베이터(678))
print("[1] result: " + 마법의엘리베이터(1000))
print("[9] result: " + 마법의엘리베이터(56))
print("[9] result: " + 마법의엘리베이터(46))
print("[11] result: " + 마법의엘리베이터(155))
print("[10] result: " + 마법의엘리베이터(55))
print("[8] result: " + 마법의엘리베이터(75))
print("[14] result: " + 마법의엘리베이터(555))
print("[22] result: " + 마법의엘리베이터(123456789))
print("[6] result: " + 마법의엘리베이터(95))
print("[9] result: " + 마법의엘리베이터(45))
print("[18] result: " + 마법의엘리베이터(5454))
print("[17] result: " + 마법의엘리베이터(5654))
print("[18] result: " + 마법의엘리베이터(5555))
print("[9] result: " + 마법의엘리베이터(65))
print("[8] result: " + 마법의엘리베이터(75))
print("[9] result: " + 마법의엘리베이터(54))
print("[9] result: " + 마법의엘리베이터(56))
print("[26] result: " + 마법의엘리베이터(57595358))