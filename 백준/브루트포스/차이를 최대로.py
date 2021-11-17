'''
6
20 1 15 8 4 10
'''
from itertools import permutations
n = int(input())
arr = list(map(int,input().split()))
result = float('-inf')
for A in list(permutations(arr,n)):
    count=0
    for i in range(n-1):
        count+=abs(A[i]-A[i+1])
    result = max(result,count)
print(result)