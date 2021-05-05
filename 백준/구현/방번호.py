N = input()
cnt = [0 for _ in range(9)]
for i in range(10):
    if i==9:
        cnt[6]+= N.count(str(i))
        continue
    cnt[i] = N.count(str(i))
cnt[6] = (cnt[6]+1)//2
print(max(cnt))


