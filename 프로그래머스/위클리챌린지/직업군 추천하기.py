def solution(table, languages, preference):
    score = {}                                                                          #직군별 점수를 담을 score딕셔너리 선언 ex) {"SI":29,"Game":35} key가 직군, value가 점수
    for t in table:                                                                     #table: 데이터가 정보가 담겨있음
        for lang, prefer in zip(languages,preference):                                  #언어와 해당 언어대한 선호도 값이 담긴 리스트을 zip으로 묶어 한번에 처리
            row = t.split()
            if lang in row:
                job_type = row[0]                                                       #row의 첫번째 인덱스는 직군유형 ex)SI,CONTENTS,GAME,HARDWARE
                score[job_type] = score.get(job_type,0) + (6-row.index(lang))*prefer    #해당 직군별 선호도를 통해 score를 갱신

    result = sorted(score.items(),key=lambda x : (-x[1],x[0]))[0][0]                    #직군별 점수가 담긴 score딕셔너리를 list형태로 바꾸고,
                                                                                        #점수를 기준으로 내림차순정렬, 점수가 동일한경우 직군 유형의 문자열을 기준으로 오른차순정렬
    return result                                                                       #정렬한 리스트에서 가장 앞에 있는 원소의 직군 유형을 리턴한다.


#입력 데이터
solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],["JAVA", "JAVASCRIPT"],[7, 5])