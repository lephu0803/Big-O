class Node:
    def __init__(self, data, left = None, right =None):
        self.data = data
        self.left = left
        self.right = right

    def add(self,x):
        if x < self.data:
            if self.left == None:
                p = Node(x)
                self.left = p
            else:
                self.left.add(x)
        elif (x > self.data):
            if self.right == None:
                p = Node(x)
                self.right = p
            else:
                self.right.add(x)
        else:
            return

    def min(self):
        if(self.left == None):
            return self.data
        else:
            return self.left.min()

class BST:
    def __init__(self):
        self.root = None

    def add(self, x):
        if (self.root == None):
            p = Node(x)
            self.root = p
        else:
            self.root.add(x)

    def min(self):
        return self.root.min()

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    bst = BST()
    for i in a:
        bst.add(i)
    
    print(bst.min())
