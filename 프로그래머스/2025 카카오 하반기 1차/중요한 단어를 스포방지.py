def solution(message, spoiler_ranges):
    res = 0
    strArr = message.split(" ")
    places = dict()
    p = 0
    b = 'z'
    for i in range(len(message)):  # 20000
        if message[i] == " ":
            places[i] = b
            p += 1
        else:
            places[i] = p

    total_word = set()
    wordArr = []
    for sr in spoiler_ranges:  # 1000
        word = set()
        for i in range(sr[0], sr[1] + 1):  # 20000
            if places[i] == b:
                continue
            word.add(places[i])
            total_word.add(places[i])
        wordArr.append(list(word))

    # 각 단어의 개수 딕셔너리 생성
    wordCnt = dict()
    for st in strArr:
        if st in wordCnt:
            wordCnt[st] += 1
        else:
            wordCnt[st] = 1
    # 스포방지 처리
    for i in total_word:
        wordCnt[strArr[i]] -= 1

    # 카운팅
    for i in total_word:
        if wordCnt[strArr[i]] == 0:
            res += 1
        wordCnt[strArr[i]] += 1

    return res

#message	spoiler_ranges	result
solution("here is muzi here is a secret message",[[0, 3], [23, 28]]) #1
solution("my phone number is 01012345678 and may i have your phone number",[[5, 5], [25, 28], [34, 40], [53, 59]])#4