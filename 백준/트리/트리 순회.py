#트리순회
'''
    A
  B   C
D    E F
        G

ABDCEFG 전위 DLR
DBAECFG 중위 LDR
DBEGFCA 후위 LRD
'''
#노드
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

#트리
class Tree:
    def __init__(self):
        self.head = None

    #1.전위순회
    def preoder(self,node,ret):
        ret.append(node.data)
        if node.left !=None: self.preoder(node.left,ret)
        if node.right !=None: self.preoder(node.right,ret)

    #2.중위순회
    def inoder(self, node, ret):
        if node.left != None: self.inoder(node.left, ret)
        ret.append(node.data)
        if node.right != None: self.inoder(node.right, ret)

    #3.후위순회
    def postoder(self, node, ret):
        if node.left != None: self.postoder(node.left, ret)
        if node.right != None: self.postoder(node.right, ret)
        ret.append(node.data)

n=int(input())
rootNode = ""
d={}
for i in range(n):
    name = chr(65+i)
    d[name] = Node(name)

for i in range(n):
    p,l,r = input().split()
    if l != '.':
        d[p].left = d[l]
    if r != '.':
        d[p].right = d[r]

tree=Tree()
root=d["A"]
ret=[]
tree.preoder(root,ret)
ret.append('\n')
tree.inoder(root,ret)
ret.append('\n')
tree.postoder(root,ret)
print(''.join(ret))