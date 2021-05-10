N = int(input())
L = input()
pi = [0]*N
j=0
for i in range(1,N):
    while j>0 and L[i]!=L[j]:
        j=pi[j-1]

    if L[i]==L[j]:
        pi[i]=j+1
        j+=1
print(N-pi[-1])
