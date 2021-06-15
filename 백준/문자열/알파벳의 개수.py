s = input()
arr = [0]*26

for i in range(26):
    alpa = chr(97+i)
    arr[i] = s.count(alpa)

print(' '.join(map(str, arr)))