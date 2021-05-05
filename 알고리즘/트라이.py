#자동 완성 및 검색어 추천 기능에서 Trie 알고리즘을 사용
#문자열의 길이가 M이라면 문자열 길이만큼의 시간복잡도가 걸림 O(M)
class Node(object):
    def __init__(self, key=None, data=None):
        self.key = key                          #문자를 저장
        self.data = data                        #마지막노드의 data에 문자열을 저장, data가 존재한다면 리프노드
        self.children = {}                      #자식노드들을 담음 key-문자, value는 해당문자의 노드주소

class Trie(object):
    def __init__(self):
        self.head = Node(None)
    #문자열 삽입
    def insert(self, st):
        cur_node = self.head
        for c in st:                            #문자열에서 하나씩 문자를 꺼내면서
            if c not in cur_node.children:      #문자가 자식노드들이 담겨있는 집합에 없다면
                cur_node.children[c]=Node(c)    #자식노드 집합에 문자에 해당하는 노드를 생성하여 삽입함
            cur_node = cur_node.children[c]     #현재노드에서 문자에 해당하는 자식노드로 이동
        cur_node.data = st                      #끝난지점에 현재노드의 data값으로 문자열 저장

    #문자열 검색
    def search(self, st):
        cur_node = self.head
        for c in st:
            if c in cur_node.children:
                cur_node=cur_node.children[c]
            else:
                return False
        if cur_node.data==st:   #마지막 노드까지 내려갔을때 해당문자열이 data에 들어있다면 True
            return True
        return False            #"abc"문자열은 존재하지만 "ab"를 검색했다면 False



trie = Trie()
trie.insert("abc")
trie.insert("ac")
trie.insert("dbc")
print(trie.head.children["a"].children)
print(trie.search("abc"))