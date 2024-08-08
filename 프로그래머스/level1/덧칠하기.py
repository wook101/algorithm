def solution(n, m, section):
    cnt = 0
    section.sort(reverse=True)
    while section:
        num = section[-1]
        for i in range(num, num+m):
            if section and i == section[-1]: #시간복잡도 고려하기 remove 쓰면 시간초과
                section.pop()
        cnt+=1
    return cnt

