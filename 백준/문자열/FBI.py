result = []
for i in range(5):
    st = input()
    if "FBI" in st:
       result.append(str(i+1))

if result:
    print(' '.join(result))
else:
    print("HE GOT AWAY!")