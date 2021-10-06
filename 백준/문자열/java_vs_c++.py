def cpp(st):
    for c in st:
        if c.isupper(): return False
    if not "_" in st: return False
    return True


def cpp_to_java(st):
    res = ""
    arr = st.split("_")
    for i in range(len(arr)):
        word = arr[i]
        if i == 0:
            res += word
            continue
        res += word[0].upper() + word[1:]
    return res


def java_to_cpp(st):
    res=""
    for c in st:
        if c.isupper():
            c=c.lower()
            res+="_"
        res+=c
    return res


def error(st):
    if st[0]=="_" or st[-1]=="_" or st[0].isupper() or "__" in st:
        return True

    for i in range(len(st)-1):
        if st[i]=="_" and st[i+1].isupper():
            return True
        if  st[i].isupper() and st[i+1]=="_":
            return True

    upper = False
    for c in st:
        if c.isupper(): upper=True
    if upper and "_" in st: return True

    return False

def solution():
    st=input()
    if error(st):
        return "Error!"
    elif cpp(st):
        return cpp_to_java(st)
    else:
        return java_to_cpp(st)

