import sys

def solution():
    n=int(sys.stdin.readline())
    k=int(sys.stdin.readline())
    sensor = list(map(int, sys.stdin.readline().split()))

    sensor.sort()
    dist = [0]*n
    for i in range(n-1):
        dist[i] = sensor[i+1]-sensor[i]

    dist.sort()
    for _ in range(k-1):
        if dist: dist.pop()

    return sum(dist)



