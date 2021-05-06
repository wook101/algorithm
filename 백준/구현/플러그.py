import sys
n=int(sys.stdin.readline())
multi =[int(sys.stdin.readline())for _ in range(n)]
print(sum(multi)-(n-1))