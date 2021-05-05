n=int(input())
ropes = [int(input()) for _ in range(n)]
ropes.sort(reverse=True)
maxW = 0
for i in range(n):
    w = ropes[i]
    maxW = max(maxW,w*(i+1))
print(maxW)