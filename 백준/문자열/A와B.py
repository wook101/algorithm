s=input()
t=list(input())

while len(s)!=len(t):
    if t[-1]=='A':
        t.pop()
    else:
        t.pop()
        t = t[::-1]

print(1 if ''.join(t)==s else 0)