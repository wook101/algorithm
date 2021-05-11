import sys
n = int(sys.stdin.readline())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
arr = sorted(arr,key=lambda k:k[0])

count = 0
x,y = arr[0][0],arr[0][1]
for i in range(1,len(arr)):
    nx,ny = arr[i]
    if x<=ny<=y:
        continue
    elif nx<=y:
        y=ny
    else:
        count += y - x
        x, y = nx, ny
print(count+y-x)

