class Student:
    def __init__(self,toan,van):
        self.toan = toan
        self.van = van
    
    def trungbinh(self):
        return (self.toan+self.van)/2

if __name__ == '__main__':
    n = int(input())
    count = 0
    for i in range(n):
        ten = input()
        x, y = map(float, input().split())
        hs = Student(x, y)
        
        if hs.trungbinh() >= 9.0:
            count += 1
        
    print(count)