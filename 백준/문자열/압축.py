def solution(S):
    stack =[]
    total,count=0,0
    for i in range(len(S)):
        if S[i]==")":
            k,pre_cnt = stack.pop()
            total=pre_cnt+k*count
            count=total
        elif S[i]=="(" and i!=0 and S[i-1]!="(":
            stack.append((int(S[i-1]),count-1))
            count=0
        else:
            count+=1

    return max(total,count)

#[골드5]
#압축을 풀어서 문자열을 만들어 길이를 체크할 경우 메모리 초과가 발생한다.
#메모리 초과를 없애기 위해 압축을 풀면서 카운팅 해야된다.
#1. "("이전에 있는 k값과 k값 이전에 있는 문자열의 길이를 stack에 넣는다.
#2. count변수는 "("앞부터 문자열의 길이를 나타낸다.
#3. ")"일때 "()"안에있는 문자열의 길이를 total에 저장하고, count값을 현재의 total값으로 변경한다.
#4. 마지막 문자가 ")"인경우 total, 아닌경우 count값을 리턴한다.

solution("33(562(71(9)))")  #19
solution("11(00)9")         #마지막이 ")"가 아닌 경우 total이 아닌 count가 정답이다.
