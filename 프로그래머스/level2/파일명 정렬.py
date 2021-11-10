def solution(files):
    tmp = []
    for file in files:
        number,head,tail = "","",""
        check=False
        for i in range(len(file)):
            if file[i].isdigit():
                if check==False and number!="": break
                number+=file[i]
                tail = file[i+1:]
                head = file[:i-len(number)+1]
                check=True
            else:
                check=False
        tmp.append((head,number,tail))
    tmp.sort(key=lambda x:(x[0].upper(),int(x[1])))
    return [''.join(t) for t in tmp]
