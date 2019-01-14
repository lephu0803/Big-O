def isPrime(x):
    if x<2:
        return False
    else:
        for i in range(2,int(x**0.5)+1):
            if (x%i==0) and not (x==i):
                return False
    return True

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
    
    def countPrime(self):
        count=0
        if self.head==None:
            return None
        else:
            cur = self.head
            while(cur!=None):
                if isPrime(cur.data):
                    count+=1
                cur = cur.next
        return count

if __name__ == "__main__":
    a = LinkedList()
    while(1):
        n = int(input())
        if n ==-1:
            break
        else:
            a.insertTail(n)
    print(a.countPrime())