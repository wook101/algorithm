st = input()
p=0
while True:
    if len(st[p:])<10:
        print(st[p:])
        break
    print(st[p:p+10])
    p+=10
