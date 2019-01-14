class Node:
    def __init__(self,x):
        self.data = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertTail(self,x):
        p = Node(x)
        if self.head==None:
            self.head=p
            self.tail=p
        else:
            self.tail.next = p
            self.tail = p
    
    def min(self):
        if self.head==None:
            return None
        else:
            minn = self.head
            cur = self.head
            while (cur!=None):
                if cur.data < minn.data:
                    minn = cur
                cur = cur.next
            return minn.data

if __name__ == "__main__":
    a = LinkedList()
    while(1):
        i = int(input())
        if i == 0:
            break
        else:
            a.insertTail(i)
        
    print(a.min())
