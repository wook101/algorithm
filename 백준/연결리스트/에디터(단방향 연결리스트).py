#단방향 연결리스트 사용
#노드의 삽입, 삭제연산에서 삽입할 위치를 찾는데 O(n)
#시간초과... 이중연결리스트로 커서에 현재노드 위치를 저장한뒤 구현해봐야겠다...
import sys
class Node:
    def __init__(self,data, next=None):
        self.data = data    #값
        self.next = next    #다음 노드 주소

class linkedList:
    def __init__(self):
        self.head = Node(None)
        self.index = 0            #현재 위치를 표현
        self.size = 0

    def addNode(self,node):       #커서 왼쪽 노드 추가 (현재 index에 노드추가)
        self.cur = self.head      #노드를 추가할 위치을 받아 해당 노드를 가져온다.
        for _ in range(self.index):
            if self.cur.next is not None:
                self.cur = self.cur.next

        node.next = self.cur.next
        self.cur.next = node
        self.index+=1
        self.size+=1

    def removeNode(self):         #커서 왼쪽 노드 삭제
        if self.index==0:
            return
        self.cur = self.head
        for _ in range(self.index-1):
            if self.cur.next is not None:
                self.cur = self.cur.next
        self.cur.next = self.cur.next.next
        self.index-=1

    def cursorMoveLeft(self):       #커서 왼쪽 이동
        if self.index!=0:
            self.index-=1

    def cursorMoveRight(self):      #커서 오른쪽 이동
        if self.index < self.size:
            self.index+=1

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

    #연결리스트 생성 및 요소 추가
    lkList = linkedList()
    for i in range(len(st)):
        lkList.addNode(Node(st[i]))

    for cmd in cmds:
        if cmd[0]=="L":  #커서 왼쪽이동
            lkList.cursorMoveLeft()
        elif cmd[0]=="D": #커서 오른쪽이동
            lkList.cursorMoveRight()
        elif cmd[0]=="B": #커서 왼쪽에 있는 문자 삭제
            lkList.removeNode()
        elif cmd[0]=="P": #cmd[1]문자를 커서 왼쪽에 추가
            lkList.addNode(Node(cmd[1]))

    return lkList.printNodes() #연결리스트 출력
