n=int(input())
levels = [int(input()) for step in range(n)]
cnt=0
for i in range(len(levels)-2,-1,-1):
    if levels[i] >= levels[i+1]:
        diff = levels[i]-levels[i+1]+1
        levels[i] -= diff
        cnt+=diff
print(cnt)
