class Node:
    def __init__(self,x):
        self.data = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
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
    
    def find2nd(self):
        if self.head==None:
            return None
        else:
            cur = self.head
            while(cur!=None):
                if cur.data > self.max:
                    self.second = self.max
                    self.max = cur.data
                cur = cur.next
        return self.second

if __name__ == "__main__":
    a = LinkedList()
    while(1):
        i = float(input())
        if int(i) ==-1:
            break
        else:
            a.insertTail(i)
    if a.length > 1:
        print('%g'%a.find2nd())
    else:
        print('-1')