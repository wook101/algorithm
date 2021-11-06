import sys
from collections import defaultdict

def solution(cards,targets):
    result = []
    data = defaultdict(int)
    for card in cards:
        data[card]+=1
    for target in targets:
        result.append(data[target])
    
    return ' '.join(map(str,result))

N = int(input())
cards = sys.stdin.readline().split()
M = int(input())
targets = sys.stdin.readline().split()
print(solution(cards,targets))
