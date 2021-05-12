#트라이 알고리즘을 응용한 문제 (개미굴 백준 14725)
class Node(object):
    def __init__(self,data):
        self.data = data
        self.children = dict()


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, strArr):
        cur_node = self.head
        for st in strArr:
            if not st in cur_node.children:
                cur_node.children[st] = Node(st)
            cur_node=cur_node.children[st]


def dfs(v):
    result = []
    stack = [(v,"")]

    while stack:
        node,layer = stack.pop()
        if None!=node.data:
            result.append(layer)
            result.append(node.data)
            result.append('\n')
        for nextNode in sorted(node.children.items(),reverse=True):
            nextlayer = "--"+layer if None!=node.data else layer
            stack.append((nextNode[1],nextlayer))

    return ''.join(result)


def solution():
    n = int(input())
    data =[list(input().split())[1:] for _ in range(n)]

    trie=Trie()
    for strArr in data:
        trie.insert(strArr)

    node = trie.head
    return dfs(node)


print(solution())