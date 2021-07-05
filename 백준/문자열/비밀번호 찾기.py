n,m = map(int, input().split())
data = {}

for _ in range(n):
    site, password = input().split()
    data[site] = password

for _ in range(m):
    search_site = input()
    print(data[search_site])