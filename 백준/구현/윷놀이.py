while True:
    try:
        a=list(map(int, input().split()))
        cnt = a.count(0)
        if cnt==0:
            print("E")
        elif cnt == 1:
            print("A")
        elif cnt == 2:
            print("B")
        elif cnt == 3:
            print("C")
        else:
            print("D")
    except EOFError:
        break