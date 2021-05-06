arrStr = [input() for _ in range(5)]
tmp=[[] for _ in range(15)]
for st in arrStr:
    for i in range(len(st)):
        tmp[i].append(st[i])
result = []
for t in tmp:
    if t:
        result.append(''.join(t))
print(''.join(result))

