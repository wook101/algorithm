st = input()
p = len(st)//2
a = st[:p]
b = st[p+1:] if len(st)%2 else st[p:]

if a[::-1]==b:
    print(1)
else:
    print(0)