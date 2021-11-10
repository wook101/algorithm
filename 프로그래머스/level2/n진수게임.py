from collections import deque

def convert(n,num,data):
    if num==0: return "0"
    tmp = deque()
    while num != 0:
        tmp.appendleft(data[num%n])
        num = num//n
    return ''.join(tmp)

    
def solution(n, t, m, p):
    data = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    st = []
    num = 0
    while len(st)<m*t:
        st.append(convert(n,num,data))
        num+=1
    st = ''.join(st)
    
    res = []
    for i in range(p-1,t*m,m):
        res.append(st[i])
    
    return ''.join(res)
