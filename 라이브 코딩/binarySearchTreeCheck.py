#이진트리가 주어졌을때 해당 트리가 이진탐색트리인지 확인하기
#이진탐색트리는 왼쪽 서브트리 노드들의 값들이 현재 노드보다 모두 작아야하며,
#            오른쪽 서브트리 노드들의 값들이 현재 모드보다 모두 커야한다.
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinaryTree:
    def __init__(self,root):
        self.root = root


def isBinerySearchTree(node):
    if node is None: return True

    leftNode = node.left
    rightNode = node.right
    if leftNode is not None and leftNode.data >= node.data:
        return False

    if rightNode is not None and rightNode.data <= node.data:
        return False

    left = isBinerySearchTree(leftNode)
    right = isBinerySearchTree(rightNode)

    return left and right


def solution():
    arr = [0]*10
    for i in range(10):
        arr[i] = Node(i)

    #트리 생성
    bt = BinaryTree(arr[5])
    bt.root.left = arr[2]
    bt.root.right = arr[7]

    bt.root.left.left = arr[1]
    bt.root.left.right = arr[3]
    bt.root.right.left = arr[6]
    bt.root.right.right = arr[8]

    bt.root.left.left.left = arr[0]
    bt.root.right.right.right = arr[9]

    #이진탐색트리 확인하기
    print(isBinerySearchTree(bt.root))


solution()