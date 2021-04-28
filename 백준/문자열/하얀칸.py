'''
.F.F...F
F...F.F.
...F.F.F
F.F...F.
.F...F..
F...F.F.
.F.F.F.F
..FF..F.
'''

chess = [ list(input()) for _ in range(8)]
cnt=0
for i in range(8):
    for j in range(8):
        if (i+j)%2==0 and chess[i][j]=='F':  #하얀칸
            cnt+=1
print(cnt)