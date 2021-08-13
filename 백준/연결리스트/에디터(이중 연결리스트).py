import sys
class Node:
    def __init__(self,data,pre=None,next=None):
        self.data = data    #값
        self.pre = pre      #이전 노드 주소
        self.next = next    #다음 노드 주소

class doubleLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.cursor = self.head

    def addNode(self,node):                 #커서 왼쪽 노드 추가
        node.pre=self.cursor                #삽입노드 pre,next주소변경
        node.next=self.cursor.next
        if self.cursor.next is not None:    #삽입다음노드 pre주소변경
            self.cursor.next.pre=node
        self.cursor.next=node               #삽입이전노드 next주소변경
        self.cursor=node                    #커서 주소변경


    def removeNode(self):                   #커서 왼쪽 노드 삭제
        if self.cursor.data is None:
            return
        self.cursor.pre.next = self.cursor.next

        if self.cursor.next is not None:
            self.cursor.next.pre = self.cursor.pre
        self.cursor = self.cursor.pre


    def cursorMoveLeft(self):               #커서 왼쪽 이동
        if self.cursor.pre is None:
            return
        self.cursor = self.cursor.pre


    def cursorMoveRight(self):              #커서 오른쪽 이동
        if self.cursor.next is None:
            return
        self.cursor = self.cursor.next


    def printNodes(self):
        self.cur = self.head.next
        res = ""
        while self.cur is not None:
            res+=self.cur.data
            self.cur = self.cur.next

        return res

def solution():
    st = sys.stdin.readline().strip()
    m = int(sys.stdin.readline())
    cmds = [list(sys.stdin.readline().split()) for _ in range(m)]

    #이중연결리스트 생성 및 요소 추가
    dList = doubleLinkedList()
    for c in st:
        dList.addNode(Node(c))


    for cmd in cmds:
        if cmd[0]=="L":  #커서 왼쪽이동
            dList.cursorMoveLeft()
        elif cmd[0]=="D": #커서 오른쪽이동
            dList.cursorMoveRight()
        elif cmd[0]=="B": #커서 왼쪽에 있는 문자 삭제
            dList.removeNode()
        elif cmd[0]=="P": #cmd[1]문자를 커서 왼쪽에 추가
            dList.addNode(Node(cmd[1]))


    return dList.printNodes()

print(solution())