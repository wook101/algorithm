from collections import deque
def bfs(S, emoticon, clipboard, visited):
    q = deque([(emoticon, clipboard, 0)])
    while q:
        e, cb, cnt = q.popleft()
        if e == S:
            print(cnt)
            break

        if e!=cb and visited[e][e] == 0:
            q.append((e, e, cnt + 1))
            visited[e][e] = 1
        if cb>0 and visited[e+cb][cb]==0:
            q.append((e + cb, cb, cnt + 1))
            visited[e + cb][cb] = 1
        if e>0 and cb>0 and visited[e-1][cb] == 0:
            q.append((e-1, cb, cnt + 1))
            visited[e-1][cb]= 1


def solution(S):
    clipboard = 0
    emotion = 1
    visited = [[0] * 10000 for _ in range(10000)]
    bfs(S, emotion, clipboard, visited)


solution(int(input()))