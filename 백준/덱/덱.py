'''
22
front
back
pop_front
pop_back
push_front 1
front
pop_back
push_back 2
back
pop_front
push_front 10
push_front 333
front
back
pop_back
pop_back
push_back 20
push_back 1234
front
back
pop_back
pop_back

'''

from collections import deque
import sys
n=int(sys.stdin.readline())
q = deque()

for _ in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0]=="push_front":
        q.appendleft(cmd[1])
    elif cmd[0]=="push_back":
        q.append(cmd[1])
    elif cmd[0]=="pop_front":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif cmd[0]=="pop_back":
        if q:
            print(q.pop())
        else:
            print(-1)
    elif cmd[0]=="size":
        print(len(q))
    elif cmd[0]=="empty":
        if q:
            print(0)
        else:
            print(1)
    elif cmd[0]=="front":
        if q:
            print(q[0])
        else:
            print(-1)
    elif cmd[0] == "back":
        if q:
            print(q[-1])
        else:
            print(-1)