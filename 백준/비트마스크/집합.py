import sys
m=int(sys.stdin.readline())
s = 0
for _ in range(m):
    cmd = sys.stdin.readline().split()
    o=cmd[0]
    x,targetBit = 0,0
    if len(cmd)>1:
        x = int(cmd[1])-1
        targetBit = (s>>x)

    if o=="add" and not targetBit & 1:
        val = 2**x
        s+=val
    elif o=="remove" and targetBit & 1:
        val = 2**x
        s-=val
    elif o=="check":
        print(1) if targetBit & 1 else print(0)
    elif o=="toggle":
        val=2**x
        s = s-val if targetBit else s+val
    elif o=="all":
        s = 2**20-1
    elif o=="empty":
        s = 0
