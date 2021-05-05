try:
    while True:
        result = [0]*4
        st = input()
        for c in st:
            if c.islower():
                result[0]+=1
            elif c.isupper():
                result[1]+=1
            elif c.isdigit():
                result[2]+=1
            elif c==" ":
                result[3]+=1
        print(' '.join(map(str,result)))
except:
    exit()