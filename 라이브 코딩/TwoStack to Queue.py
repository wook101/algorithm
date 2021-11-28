class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    def push(self,element):
        self.stack1.append(element)


    def pop(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2.pop()
        return None


def solution(arr):
    q = Queue()

    for num in arr:
        q.push(num)

    for _ in range(len(arr)):
        print(q.pop())


solution([1,2,3,4,5,6,7,8,9,10])