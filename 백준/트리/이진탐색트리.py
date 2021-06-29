import sys
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root):
        self.root = root
        self.C = 0

    def insert(self, X, N):
        self.C += 1
        if X < N.data:
            if N.left is None:
                N.left = Node(X)
            else:
                self.insert(X, N.left)
        else:
            if N.right is None:
                N.right = Node(X)
            else:
                self.insert(X, N.right)

def solution():
    n=int(sys.stdin.readline())
    arr = [int(sys.stdin.readline()) for _ in range(n)]
    root = Node(arr[0])
    tree = Tree(root)
    if n==1: return "0"

    res = [0]
    for i in range(1,n):
        X = arr[i]
        tree.insert(X,root)
        res.append(tree.C)


    return "\n".join(map(str,res))

print(solution())

# [백준 2957번]
# 이진탐색트리 구현완료, but 최대 n=300,000이고, 시간복잡도는 O(n^2)이기 때문에 시간초과 발생 // 연산량 900억
# 다른 방법 생각 해봐야 됨