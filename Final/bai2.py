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

    def search(self, b, left, right):
        if isContain(b):   
            if left > right:
                return -1
            else:
                tmp = (left + right)//2
                if a[tmp]==x:
                    return tmp+1
                elif a[tmp]>x:
                    return search(a,x,left,tmp-1)       
                else:
                    return search(a,x,tmp+1,right)`
        

    # def search(self, b, left, right):
    #     if isContain(a) == 1:
    #         b_cur = self.head
    #         while (b_cur!=None):
    #             if self.head >= b_cur:
    #                 self.head >= b_cur
    #             cur = cur.next
    #         return minn.data

    #         if left > right:
    #             return -1
    #         else:
    #             tmp = (left + right)//2
    #             if a[tmp]==x:
    #                 return tmp+1
    #             elif a[tmp]>x:
    #                 return search(a,x,left,tmp-1)       
    #             else:
    #                 return search(a,x,tmp+1,right)

    def isContain(self,b):
    if self.head >= b.tail:
        return True
    elif b.head >= self.tail:
        return True
    return False

# def isContain(a,b):
#     if a.head >= b.tail:
#         if b.tail>=a.tail:
            
#     elif b.head >= a.tail:
#         return True
#     return False
    
# def cut(a, b):
    
if __name__ == "__main__":
    a = LinkedList()
    while True:
        x = int(input())
        if x = -1:
            break
        else: 
            a.insertTail()
    b=LinkedList()
    while True:
        x = int(input())
        if x = -1:
            break
        else: 
            b.insertTail()
    
    if isContain(a,b):
