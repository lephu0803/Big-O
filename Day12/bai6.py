class Node:
    def __init__(self,x):
        self.data = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def insertTail(self,x):
        p = Node(x)
        self.length+=1
        if self.head==None:
            self.head=p
            self.tail=p
        else:
            self.tail.next = p
            self.tail = p

    def delete_Head(self):
        self.length -=1
        self.head = self.head.next

    def printList(self):
        # count=1
        if self.head==None:
            return None
        else:
            cur = self.head
            while(cur!=None):
                print('%d'%cur.data)
                cur = cur.next
                # count+=1

if __name__ == "__main__":
    n = int(input())
    a=LinkedList()
    for i in range(n):
        number = input().split()
        if len(number) == 2:
            a.insertTail(int(number[1]))
        else:
            if a.length != 0:
                a.delete_Head()
    a.printList()

