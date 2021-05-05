
N,M = map(int, input().split())
S = set()
cnt=0
for _ in range(N):
    S.add(input())
for _ in range(M):
    st = input()
    if st in S:
        cnt+=1
print(cnt)
