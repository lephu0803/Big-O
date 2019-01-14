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

    def below5(self):
        if self.head==None:
            return None
        else:
            cur = self.head
            while(cur!=None):
                if cur.data < 5:
                    print('%g'%cur.data)
                cur = cur.next
    
    # def countPrime(self):
    #     count=0
    #     if self.head==None:
    #         return None
    #     else:
    #         cur = self.head
    #         while(cur!=None):
    #             if isPrime(cur.data):
    #                 count+=1
    #             cur = cur.next
    #     return count

    def printList(self):
        count=1
        if self.head==None:
            return None
        else:
            cur = self.head
            while(cur!=None):
                print('%d %d'%(count, cur.data), end=' ')
                cur = cur.next
                count+=1
    
    def notEnd5(self):
        if self.head==None:
            return None
        else:
            cur = self.head
            while(cur!=None):
                if cur.data%10!=5:
                    print(cur.data, end=' ')
                cur = cur.next
                
    
if __name__ == "__main__":
    n = int(input())
    a=LinkedList()
    for i in range(n):
        k =int(input())
        a.insertTail(k)
    a.notEnd5()