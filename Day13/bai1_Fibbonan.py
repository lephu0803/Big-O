class Node:
    def __init__(self,x):
        self.data = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.previous = None
        self.tail = None
        self.length = 0
        self.max = -1
        self.second = -1

    def insertTail(self,x):
        p = Node(x)
        self.length+=1
        if self.head==None:
            self.head=p
            self.tail=p
        else:    
            self.tail.next = p
            self.previous = self.tail
            self.tail = p

    def printList(self):
        # count=1
        if self.head==None:
            return None
        else:
            cur = self.head
            while(cur!=None):
                print('%d'%cur.data, end=' ')
                cur = cur.next

    def delete_Head(self):
        self.length -=1
        self.head = self.head.next

    def calNextNode(self):
        self.insertTail((self.previous.data+self.tail.data)%1000007)

if __name__ == "__main__":
    x,y,n = map(int,input().split())
    a = LinkedList()
    a.insertTail(x)
    a.insertTail(y)
    for i in range(n-2):
        a.calNextNode()
    a.printList()