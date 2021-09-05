#양방향 링크드 리스트를 사용하여 알고리즘 연산 수행 시간을 줄여본다.
#현재 선택된 행을 cursor로 표현
#n: 표의 행 개수
#k: 선택된 행의 위치

class Node:
    def __init__(self,number=None):
        self.pre = None             #pre: 이전 행의 주소  (주소)
        self.next = None            #next: 다음 행의 주소 (주소)
        self.number = number        #number: 현재 행의 번호 (값)

class dubleLinkedList:
    def __init__(self):
        self.head = Node()          #head노드 생성
        self.cursor = Node()        #현재 행을 가르키고 있는 cursor
        self.stack = []             #삭제한 행을 저장하기 위한 스택

    def init_connect(self,n):       #양방향 링크드 리스트 생성후 연결하기, head<->0<->1<->2<->3<->4<->5<->6<->7
        tmp = self.head
        for number in range(n):
            node = Node(number)
            tmp.next = node
            node.pre = tmp
            tmp = tmp.next

    def init_cursor(self,k):        #커서를 k위치에 있는 노드를 가르키도록 설정
        tmp = self.head
        for _ in range(k+1):
            self.cursor = tmp.next
            tmp = tmp.next

    def move_up(self,x):            #커서를 x만큼 위로 이동
        for _ in range(x):
            if self.cursor.pre.number is not None:
                self.cursor = self.cursor.pre

    def move_down(self,x):          #커서를 x만큼 아래로 이동
        for _ in range(x):
            if self.cursor.next is not None:
                self.cursor = self.cursor.next

    def remove(self):               #현재 커서위치의 행 제거
        self.stack.append([self.cursor,self.cursor.pre])
        if self.cursor.next is None:    #제거할 행이 마지막인 경우
            self.cursor = self.cursor.pre
            self.cursor.next=None
        else:
            self.cursor.pre.next = self.cursor.next
            self.cursor.next.pre = self.cursor.pre
            self.cursor = self.cursor.next

    def restore(self):              #가장 최근에 삭제한 행 복구, stack이용
        if self.stack:
            reNode,rePreNode = self.stack.pop()
            #복구할 행이 마지막인경우
            if rePreNode.next is None:
                rePreNode.next = reNode
            else:
                reNode.pre = rePreNode
                reNode.next = rePreNode.next
                reNode.next.pre = reNode
                rePreNode.next = reNode

    def ret(self,n):        #더블 링크트 리스트의 요소들을 탐색해서 결과값 리턴
        res=["X"]*n
        tmp = self.head
        while tmp.next is not None:
            tmp=tmp.next
            res[tmp.number]="O"
        return ''.join(res)

def solution(n, k, cmd):
    dll = dubleLinkedList()
    dll.init_connect(n)     #행의 개수(n) 만큼 노드 연결하기
    dll.init_cursor(k)      #cursor를 k위치로 설정

    for c in cmd:
        cm = c.split(" ")
        if cm[0]=="U":
            dll.move_up(int(cm[1]))
        elif cm[0]=="D":
            dll.move_down(int(cm[1]))
        elif cm[0]=="C":
            dll.remove()
        elif cm[0]=="Z":
            dll.restore()

    return dll.ret(n)


solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])             #"OOOOXOOO"
solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])   #"OOXOXOOO"