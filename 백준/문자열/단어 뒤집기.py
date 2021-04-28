'''
2
I am happy today
We want to win the first prize
'''

n=int(input())
stArr = [input() for _ in range(n)]
for st in stArr:
    tmp = []
    for s in st.split():
        tmp.append(s[::-1])
    print(' '.join(tmp))